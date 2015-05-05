import sys
import bluetooth
sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

if len(sys.argv) < 2:
    print "usage: l2capclient.py <addr>"
    sys.exit(2)

bt_addr=sys.argv[1]
port = 0x1001

print "trying to connect to %s on PSM 0x%X" % (bt_addr, port)

sock.connect((bt_addr, port))

print "connected.  type stuff"
while True:
    data = raw_input()
    if(len(data) == 0): break
    sock.send(data)

sock.close()