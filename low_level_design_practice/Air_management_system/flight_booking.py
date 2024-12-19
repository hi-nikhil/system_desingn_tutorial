from payment import Payment
from refund import Refund

class FlightBookingSystem():
    def __init__(self):
        self.flights = {}
        self.reservations = {}
        self.payment  = Payment()
        self.refund = Refund()

    def add_flights(self, flight):
        id = len(self.flights)
        self.flights[id] = flight

    def book_ticket(self, seat, passenger, flight):
        flight.book_seat(seat, passenger, self.payment) 