from car_booking_status import CarBookingStatus
from Car import Car
from User import User
from car_rental_system import CarRentalSystem

bmw = Car('BMW','C6','2021','bmw1232',1500)
alto = Car('Alto','a2','2022','alto123',500)

nikhil = User('nikgil','9239432442','licen123')
ankit = User('ankit','92383843','jksdfad')

system = CarRentalSystem()
system = CarRentalSystem()

system.add_car(bmw)
system.add_car(alto)

available_cars = system.check_availability()
for car in available_cars:
    print(f'Car {car.brand} for rental : {car.rental_per_day} is available')
print('\n')


system.book_car(nikhil,bmw)

available_cars = system.check_availability()
for car in available_cars:
    print(f'Car {car.brand} for rental : {car.rental_per_day} is available')


rent = system.unbook_car(nikhil)
available_cars = system.check_availability()
for car in available_cars:
    print(f'Car {car.brand} for rental : {car.rental_per_day} is available')

system.pay_rent(rent)

