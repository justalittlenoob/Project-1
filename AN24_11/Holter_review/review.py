import socket
import threading
import re
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('conf.ini')

HOST = config.get('Server', 'HOST')
PORT = config.getint('Server', 'PORT')

print HOST, PORT

CBLOCK_STR_LEN = 76
COUNT_STR_LEN = 54    #count block
NBLOCK_STR_LEN = 36
NBLOCK_SNR_TAG = '53'   # S
HEART_RATE_RESOLUTION = 0.25
TOTO_RESOLUTION = 0.5
SNR = 0.0
ELECTRODE_STR_LEN = 20

class ReviewClient():
    def __init__(self):
        self._sock = self.build_connection()
        self.his_patient = {}
        self.his_data = []
        self.his_info = {}
        self.his_note = []
#----------------------------

    def build_connection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception, msg:
            print msg
            print '[Fail] creat socket[review]'
        else:
            print '[ok] creat socket[review]'
        
        try:
            s.connect((HOST, PORT))
        except Exception, msg:
            print msg
            print '[Fail] connect to server[review]'
        else:
            print '[ok] connect to server[review]'
        
        return s

#-----------------------------

    def get_his_p(self,
                  _number='10',
                  _person_num='000000000000000000',
                  _time_begin='0000-00-00 00:00:00',
                  _time_end='0000-00-00 00:00:00',
                  _name='None',
                  switch='open'):
        self._get_his_p(_number,_person_num,_time_begin,_time_end,_name)

#------------------------------

    def review(self,_uuid, switch='open'):
        if switch == 'open':
            threading.Thread(target=self._review,
                            args=(_uuid,)
                            ).start()
        elif switch == 'close':
            threading.Thread(target=self._download,
                            args=(_uuid,)
                            ).stop()

#------------------------------#

##--------------------------

    def _get_his_p(self, _number,_person_num, _time_begin, _time_end, _name):
        try:
            self._sock.send('GHP'+
                           _number+
                           _person_num + 
                           _time_begin+
                           _time_end + 
                           _name + 
                           '\r\n') #GHP=Get History Patients
        except Exception, msg:
            print msg
            print '[Fail] send get history patient request'
        else:
            print '[ok] send get history patient request'
        buf = self._sock.recv(65535)
        self.his_patient = eval(buf[3:])
        print 'his_patient:', self.his_patient

##---------------------------

    def _review(self, _uuid):
        try:
            self._sock.send('DHPD' + 
                             _uuid + 
                             '\r\n')#DCPD=Download History Patient Data
        except Exception, msg:
            print msg
            print '[Fail] send download current patient data request'
        else:
            print '[ok] send download current patient data request'
        lbuf = ''
        endstr ='1003'
        while 1:
            pattern = re.compile(r'1002.*?1003', re.DOTALL)
            buf = self._sock.recv(65535)
            if buf[:5] == 'HINFO':
                self.info = eval(buf[5:])
                print 'HINFO:', self.info

            else:
                lbuf = lbuf + buf
                for m in pattern.finditer(lbuf):
                    #print '[raw data:]', m.group()
                    if m.group()[4:9] == 'HNOTE':
                        print 'm[hnote]', m.group()
                        note = eval(m.group()[9:-4])
                        self.his_note.append(note)
                        print 'HNOTE:', self.note
                    else:
                        self.handle_data(m.group())
                while endstr in lbuf:
                    endpos = lbuf.index(endstr) + 4 
                    lbuf = lbuf[endpos:]

##-----------------------

    def handle_data(self, cblock_str):
        mm = '10024d4d1003'                 # MM block
        low_battry = '10024e3032414eB1003'  #low battry
        event = 0
        FHR = []
        MHR = []
        TOCO = 0
        mother_mv = []
        data_one_sec = []
        #init_An24.run_check(cblock_str)
        if(len(cblock_str) == CBLOCK_STR_LEN):
        
            FHR_split = [10, 14, 18, 22, 26]
            MHR_split = [42, 46, 50, 54, 58]
            TOCO_split = [58, 60, 62, 64, 66]

            FHR_section = [
                    cblock_str[FHR_split[0]:FHR_split[1]],
                    cblock_str[FHR_split[1]:FHR_split[2]],
                    cblock_str[FHR_split[2]:FHR_split[3]],
                    cblock_str[FHR_split[3]:FHR_split[4]]
                    ]
            MHR_section = [
                    cblock_str[MHR_split[0]:MHR_split[1]],
                    cblock_str[MHR_split[1]:MHR_split[2]],
                    cblock_str[MHR_split[2]:MHR_split[3]],
                    cblock_str[MHR_split[3]:MHR_split[4]]
                    ]
            TOCO_section = [
                    cblock_str[TOCO_split[0]:TOCO_split[1]],
                    cblock_str[TOCO_split[1]:TOCO_split[2]],
                    cblock_str[TOCO_split[2]:TOCO_split[3]],
                    cblock_str[TOCO_split[3]:TOCO_split[4]]
                    ]
                        
            FHR_section = [int_16(f) for f in FHR_section]
            MHR_section = [int_16(m) for m in MHR_section]
            TOCO_section = [int_16(t) for t in TOCO_section]

            for fh_s in FHR_section:
                fh = round(int(fh_s & 0x7FF) * HEART_RATE_RESOLUTION, 2)
                FHR.append(fh)

            for mh_s in MHR_section:
                mh =round(int(mh_s&0x7ff) * HEART_RATE_RESOLUTION, 2)
                m_mv = int((mh_s&0x1800) >> 11)
                mother_mv.append(m_mv)
                MHR.append(mh)
        
            for to_s in TOCO_section:
                TOCO = int(int(to_s) * TOTO_RESOLUTION)
        
        
       
        elif len(cblock_str) == NBLOCK_STR_LEN:
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]
            '''Compute the SNR from N block'''
            if cblock_str[14:16] == NBLOCK_SNR_TAG:
                global SNR
                fetal_signal = int(cblock_str[16:24], 16)
                noise = int_16(cblock_str[24:32])          #int(cblock_str[24:32], 16)
                SNR_func = lambda x, y : round(x / float(y), 4)
                SNR = SNR_func(fetal_signal,
                               noise)
             
                #print 'SNR:', SNR
            else:
                pass
            return 

        elif cblock_str == mm:          #event
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]

            event = 1
         
        elif cblock_str == low_battry:
            #FHR = [0, 0, 0, 0]
            #MHR = [0, 0, 0, 0]
            #mother_mv = [0, 0, 0, 0]
            #init_An24.LOW_BATTRY = True
            self.low_battry[0] = True
            return

        else:
            return
            '''
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]
            '''

        data_one_sec.append([FHR[0], MHR[0], TOCO, mother_mv[0], SNR, event])
        data_one_sec.append([FHR[1], MHR[1], TOCO, mother_mv[1], SNR, event])
        data_one_sec.append([FHR[2], MHR[2], TOCO, mother_mv[2], SNR, event])
        data_one_sec.append([FHR[3], MHR[3], TOCO, mother_mv[3], SNR, event])
        for data_os in data_one_sec:
            self.his_data.append(data_os)
##----------------------------##

def int_16(x, base = 16):
	return int(x, base)

if __name__ == '__main__':
    rc = ReviewClient()
    rc.review('cc0b9e00-69a2-11e5-a614-1078d2f63bb4')
