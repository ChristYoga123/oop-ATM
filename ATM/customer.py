from ctypes.wintypes import PINT
import atm_card

class Customer:
    # constructor
    def __init__(self, id, pin=1234, balance=10000) -> None:
        self.id = id
        self.pin = pin
        self.balance = balance

    def getId(self):
        return self.id
    
    def getPin(self):
        return self.pin

    def getBalance(self):
        return self.balance

    def withdraw(self, nominal):
        self.balance-=nominal

    def deposit(self, nominal):
        self.balance+=nominal
    
