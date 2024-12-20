from datetime import datetime
from car_booking_status import CarBookingStatus

class Car():
    def __init__(self,brand, model, year, license, rental_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.license = license
        self.rental_per_day = rental_per_day
        self.assigned_user = None
        self.booked_date = None
        self.status = CarBookingStatus.IDLE
    
    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_license(self):
        return self.license
    
    def get_rental_per_day(self):
        return self.rental_per_day
    
    def get_assigned_user(self):
        return self.assigned_user
    
    def get_booked_date(self):
        return self.booked_date
    
    def get_status(self):
        return self.status
    
    def assign_car(self,user):
        self.assigned_user = user
    
    def update_status(self,status):
        # print(f'updating car status from car:{self.model} to status:{status}')
        self.status = status
        # print(f'current status:{self.status}')
    
    def update_booked_date(self,date):
        self.booked_date = date
    
    def unassign_car(self):
        self.assigned_user = None
        