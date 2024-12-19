from flight_booking import FlightBookingSystem
from passenger import Passenger
from flight import Flight

flight_booking_system = FlightBookingSystem()

p1 = Passenger('nik','nik@gmai;,com','address','22',[])

f1 = Flight('1','de;hi','banglore','12312','1231221',10)

seats = f1.get_availability()
for seat in seats:
    print(f'seat : {seat.id}, type: {seat.type}')

flight_booking_system.add_flights(f1)

flight_booking_system.book_ticket(seats[0],p1,f1)

seats = f1.get_availability()
for seat in seats:
    print(f'seat : {seat.id}, type: {seat.type}')