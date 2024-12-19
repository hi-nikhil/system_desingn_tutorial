from reservation_status import ReservationStatus

class Reservation():
    def __init__(self, id, passenger, flight, amount, seat):
        self.id = id
        self.passenger = passenger
        self.flight = flight
        self.amount = amount
        self.status = ReservationStatus.BOOKED
        self.seat = seat
    
    def get_flight(self):
        return self.flight
    
    def get_passenger(self):
        return self.passenger
    
    def get_amount(self):
        return self.amount
    
    def get_status(self):
        return self.status
    
    def update_status(self, status):
        self.status = status
     
    def get_seat(self):
        return self.seat
        