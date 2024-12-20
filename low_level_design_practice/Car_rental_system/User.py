class User():
    def __init__(self, name, contract_details, license):
        self.name = name
        self.contact_details = contract_details
        self.license = license
    
    def get_name(self):
        return self.name
    
    def get_contact_details(self):
        return self.contact_details
    
    def get_license(self):
        return self.license
        