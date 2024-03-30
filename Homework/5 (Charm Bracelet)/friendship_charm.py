# Define your FriendshipCharm class here
# This class should inherit from Charm

from charm import Charm

class FriendshipCharm(Charm):
    def __init__(self, name, description, retailPrice, condition, symbol):
        super().__init__(name, description, retailPrice, condition)
        self.__symbol = symbol
        
    def getMarketValue(self):
        return round(self.getCondition().value / 100, 2)
    
    def getSymbol(self):
        return self.__symbol

    def __str__(self):
        return self.__symbol
  
    def __lt__(self, other):
        return self.getMarketValue() < other.getMarketValue()

    def __le__(self, other):
        return self.getMarketValue() <= other.getMarketValue()

    def __gt__(self, other):
        return self.getMarketValue() > other.getMarketValue()

    def __ge__(self, other):
        return self.getMarketValue() >= other.getMarketValue()
    
    def __eq__(self, other):
        return self.getMarketValue() == other.getMarketValue()
    
    def __ne__(self, other):
        return self.getMarketValue() != other.getMarketValue()