import threading

class CashDispenser():
    def __init__(self, available_balance):
        self.available_balance = available_balance
        self.lock = threading.Lock()
    
    def dispense_cash(self,amount):
        if amount > self.available_balance:
            raise ValueError('Insufficient cash balance in ATM')
        self.available_balance -= amount
        print(f'Cash dispense :{amount}')
        