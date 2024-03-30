# Author: David Miller | djm545
# Date: 4/12/2023
# Purpose: This is the item class that creates a single item to be purchased

class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
    
    def itemToString(self):
        return "{:_<20}".format(f"{self.__name}") + "{:_>20}".format(f"{self.__price:.2f}")
    
    def getPrice(self):
        return self.__price
    
    def getTax(self, taxRate):
        if self.__taxable:
            return self.__price * taxRate
        else:
            return 0