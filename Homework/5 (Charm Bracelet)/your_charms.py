

# Add at least one new subclass of Charm here.
from charm import Charm
from enum import Enum

class StarWarsCharm(Charm):
    class Alignment(Enum):
        UNALIGNED = 9
        # Sequel Trilogy
        FIRST_ORDER = 8
        NEW_REPUBLIC = 7
        # Original Trilogy
        EMPIRE = 6
        REBELLION = 5
        # Prequel Trilogy
        GALACTIC_REPUBLIC = 4
        CONFEDERACY_OF_INDEPENDENT_SYSTEMS = 3
        # Old Republic
        OLD_REPUBLIC = 2
        SITH_EMPIRE = 1
    
    def __init__(self, name, description, retailPrice, condition, alignment):
        super().__init__(name, description, retailPrice, condition)
        self.setAlignment(alignment)
        
    def getMarketValue(self):
        return round((self.getCondition().value / 100), 2)
    
    def getAlignment(self):
        return self.__alignment
    
    def setAlignment(self, alignment):
        if not isinstance(alignment, Charm.Alignment):
            raise Exception("Alignment value must be of type StarWarsCharm.Alignment")
        self.__alignment = alignment
        
    def isDirectRival(self, other):
        return True if self.getAlignment().value + 1 // 2 == other.getAlignment().value + 1 // 2 else False
        
    def isHostile(self, other):
        return True if self.getAlignment().value % 2 == other.getAlignment().value % 2 else False

    def __str__(self):
        return self.__alignment
  
    def __lt__(self, other):
        return self.getMarketValue() < other.getMarketValue()

    def __le__(self, other):
        return self.getMarketValue() <= other.getMarketValue()

    def __gt__(self, other):
        return self.getMarketValue() > other.getMarketValue()

    def __ge__(self, other):
        return self.getMarketValue() >= other.getMarketValue()
    
    def __eq__(self, other):
        return self.__alignment == other.getAlignment()
    
    def __ne__(self, other):
        return self.__alignment != other.getAlignment()



# Write code below that tests your new class
if __name__ == "__main__":
    charm1 = StarWarsCharm("CIS", "Charm of the Confederacy of Independent Systems", 2.99, Charm.Condition.VERY_GOOD, StarWarsCharm.Condition.CONFEDERACY_OF_INDEPENDENT_SYSTEMS)
    charm2 = StarWarsCharm("GR", "Charm of the Galactic Republic", 2.99, Charm.Condition.VERY_GOOD, StarWarsCharm.Condition.GALACTIC_REPUBLIC)
    charm3 = StarWarsCharm("GR", "Charm of the Galactic Republic", 2.99, Charm.Condition.WORN, StarWarsCharm.Condition.GALACTIC_REPUBLIC)