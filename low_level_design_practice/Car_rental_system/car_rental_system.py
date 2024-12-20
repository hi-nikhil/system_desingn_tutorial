from datetime import datetime
from car_booking_status import CarBookingStatus

class CarRentalSystem():
    _instance = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__new__(self,*args, **kwargs)
            self._instance.cars = [] 
            self._instance.users = {}
        else:
            print('Instance already created')
        return self._instance
    
    def add_car(self,car):
        self.cars.append(car)
    
    def check_availability(self):
        available_cars = []
        for car in self.cars:
            if car.get_status() == CarBookingStatus.IDLE:
                available_cars.append(car)
        return available_cars
    
    def book_car(self, user, car):
        if car.get_status() == CarBookingStatus.BOOKED:
            raise ValueError('Car is already booked')
        
        if user in  self.users:
            raise ValueError('User already has a car booked to his name')
        print(f'Car :{car.model} is booked by {user.name}')
        car.assign_car(user)
        car.update_status(CarBookingStatus.BOOKED)
        car.update_booked_date(datetime.now())
        self.users[user] = car

    def unbook_car(self,user):
        booked_car = self.users[user]     
        print(f'unbooking car {booked_car.model} by {user.name}')
        rent = self.calculate_rent(booked_car)
        booked_car.unassign_car()
        booked_car.update_status(CarBookingStatus.IDLE)
        booked_car.update_booked_date(None)   
        self.users.pop(user,None)
        return rent
    
    def calculate_rent(self, booked_car):
        booked_date = booked_car.get_booked_date()
        rent_per_day = booked_car.get_rental_per_day()
        current_day = datetime.now()
        booking_days = (current_day - booked_date).days
        return (booking_days+10) * rent_per_day
    
    def pay_rent(self,rent):
        print(f'Paying rent for amount: {rent}')


         
