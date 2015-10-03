import AN24, Patient
from handler import Handler
class UiAN24():
    def __init__(self, name, address):
        self.rawAN24= AN24.AN24({name:address})
        self.handler = Handler(self.rawAN24._uuid, self.rawAN24._name)
        self.patient = Patient.Patient()
        self.address = address
        self.name = name
        self.all_battry_time = 10.0
        self.rest_battry_time = 0
        self.start_time = 0               
        self.draw_current_time = 0
        self.is_detecting = False
        self.is_infoed = False
        self.is_connected = False
        self.is_checked = False
        self.end_count_pre = 0        
        self.note = []

if __name__ == '__main__':
    an24 = UiAN24('likun', 'fdsafsaf')
    print an24.patient.age
