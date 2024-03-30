# Author: David Miller | djm545
# Date: 4/12/2023
# Purpose: This is the receipt that compiles all of the items together and
#		   sends it all back to main to be printed

import datetime

class Receipt:
    
    def __init__(self, taxRate):
        self.__tax_rate = taxRate
        self.__purchases = []
        
    def addItem(self, Item):
        self.__purchases.append(Item)
        
    def getSubTotal(self):
        subTotal = 0
        for i in self.__purchases:
            subTotal += i.getPrice()
        return subTotal
    
    def getTaxAmount(self):
        taxAmount = 0
        for i in self.__purchases:
            taxAmount += i.getTax(self.__tax_rate)
        return taxAmount
    
    def receiptToString(self):
        #string = f"----- Receipt {datetime.datetime.now()} -----\n"
        string = f"----- Receipt time -----\n"
        for i in self.__purchases:
            string += i.itemToString() + "\n"
        string += "\n{:_<20}".format("Sub Total") + "{:_>20}".format(f"{self.getSubTotal():.2f}")
        string += "\n{:_<20}".format("Tax") + "{:_>20}".format(f"{self.getTaxAmount():.2f}")
        string += "\n{:_<20}".format("Total") + "{:_>20}".format(f"{self.getSubTotal() + self.getTaxAmount():.2f}")
        return string