# Atm Card
class ATMCard:
    defaultPin = 0
    defaultBalance = 0
    # constructor
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def getPin(self):
        return self.defaultPin
    
    def getBalance(self):
        return self.defaultBalance