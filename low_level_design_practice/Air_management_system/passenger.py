class Passenger():
    def __init__(self, name, email, address, age, baggage):
        self.name = name
        self.email = email
        self.address = address
        self.age = age
        self.baggage = []
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_address(self):
        return self.address
    
    def get_age(self):
        return self.age
    
    def get_baggage(self):
        return self.baggage