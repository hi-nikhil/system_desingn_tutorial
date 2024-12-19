from seat import Seat
from seat_type import SeatType
from seat_status import SeatStatus
from seat import Seat
from payment import Payment
from reservation import Reservation
from refund import Refund
from reservation_status import ReservationStatus

class Flight():
    def __init__(self, id, source, destination, departure, arrival, num_of_seats):
        self.id = id
        self.source = source
        self.destination = destination
        self.arrival = arrival
        self.departure = departure
        seats = []
        for i in range(num_of_seats):
            if i < num_of_seats/3:
                seats.append(Seat(i,SeatType.AISLE))
            elif i < num_of_seats / 1.5:
                seats.append(Seat(i,SeatType.MIDDLE))
            else:
                seats.append(Seat(i, SeatType.WINDOW))
        self.seats = seats
    
    def get_source(self):
        return self.source
    
    def get_destination(self):
        return self.destination
    
    def get_arrival(self):
        return self.arrival
    
    def get_departure(self):
        return self.departure
    
    def get_availability(self):
        available_seats = []
        for seat in self.seats:
            if seat.get_status() == SeatStatus.AVAILABLE:
                available_seats.append(seat)
        return available_seats
    
    def book_seat(self, seat: Seat, passenger, payment: Payment):
        print(f'Booking seat: {seat.id} fro passenger: {passenger.name} in flight:{self.id}')
        seat_cost = seat.type.value
        payment_status = payment.completer_payment(seat_cost)
        if payment_status:
            reservation = Reservation(self.id+passenger.name,passenger,self,seat_cost,seat)
            seat.set_status(SeatStatus.OCCUPIED)
            print(f'Booking seat: {seat.id} fro passenger: {passenger.name} in flight:{self.id}')
            print(f'Reservation id:{reservation.id}')
        else:
            raise ValueError('payment failed')
    
    def cancel_seat(self, reservation: Reservation, refund: Refund):
        print(f'Cancelling booking for {reservation.seat_number} ')
        refund_cost = reservation.get_amount()
        refund_status = refund.completer_payment(refund_cost)
        seat = reservation.get_seat()
        if refund_status:
            reservation.update_status(ReservationStatus.REFUNDED)
            seat.set_status(SeatStatus.AVAILABLE)
            print(f'Cancellation complete seat: {seat.id}  in flight:{self.id}')
            print(f'Reservation id:{reservation.id}')
        else:
            raise ValueError('payment failed')

