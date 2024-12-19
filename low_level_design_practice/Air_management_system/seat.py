from seat_status import SeatStatus

class Seat():
    def __init__(self, id, type):
        self.id = id
        self.status = SeatStatus.AVAILABLE
        self.type = type
        self.passenger = None
    
    def get_status(self):
        return self.status
    
    def get_passenger(self):
        return self.passenger
    
    def get_type(self):
        return self.type
    
    def set_status(self, status):
        self.status = status
    
    def set_passenger(self, passenger):
        self.passenger = passenger
    

        