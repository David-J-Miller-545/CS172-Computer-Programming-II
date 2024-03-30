# Add Imports Here
from linked_list import LinkedList, Node
from charm import Charm

# Define Bracelet Class Here
class Bracelet(LinkedList):
    def __init__(self, braceletValue):
        super().__init__()
        self.__braceletValue = braceletValue
        
    def append(self, data):
        #if self.isClosed():
            #self.open()
        if isinstance(data, Charm):
            super().append(data)
        #if self.isOpen():
            #self.close()
        
    def appraise(self):
        appraisalValue = 0
        for x in range(0, len(self) - 1):
            appraisalValue += self[x].getMarketValue()
        return round(appraisalValue + self.__braceletValue)
    
    def open(self):
        if not self.isEmpty():
            self[len(self)].setNext(None)
    
    def close(self):
        if not self.isEmpty():
            self[len(self)].setNext(self.getHead())
        
    def isOpen(self):
        if self.isEmpty():
            return True
        else:
            return True if self[len(self)].getNext() == None else False
    
    def isClosed(self):
        return not(self.isOpen())
    
    def __len__(self):
        length = 0
        for x in range(1, super().__len__()):
            if self[x] == self.getHead():
                length = x - 1
                break
        return length
        
        