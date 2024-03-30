# Define your CollectibleCharm class here
# This class should inherit from Charm

from charm import Charm

class CollectibleCharm(Charm):
    def __init__(self, name, description, retailPrice, condition, serialNumber):
        super().__init__(name, description, retailPrice, condition)
        self.__serialNumber = serialNumber
        
    def getMarketValue(self):
        return round(((self.getRetailPrice() * self.getCondition().value) / 100), 2)
    
    def getSerialNumber(self):
        return self.__serialNumber

    def __str__(self):
        return f'{self.getName()} [{self.__serialNumber}]'
  
    def __lt__(self, other):
        return self.getMarketValue() < other.getMarketValue()

    def __le__(self, other):
        return self.getMarketValue() <= other.getMarketValue()

    def __gt__(self, other):
        return self.getMarketValue() > other.getMarketValue()

    def __ge__(self, other):
        return self.getMarketValue() >= other.getMarketValue()
    
    def __eq__(self, other):
        return True if (self.getName() == other.getName() and self.getDescription() == other.getDescription() and self.getRetailPrice == other.getRetailPrice and self.getCondition().value == other.getCondition().value and self.__serialNumber == other.getSerialNumber()) else False
    
    def __ne__(self, other):
        return True if not(self == other) else False
