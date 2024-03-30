# Author: David Miller | djm545
# Date: 4/12/2023
# Purpose: Asks the user for items to purchace, their price, and if they are taxable
#		   and prints a receipt that details the time it was printed, each item, 
#		   the sub total, and the total cost.

from item import Item
import receipt

#Main Program
if __name__=="__main__":
    print("Welcome to Receipt Creator")
    taxRate = .07
    userReceipt = receipt.Receipt(taxRate)
    while True:
        itemName = input("Enter Item name: ")
        itemPrice = float(input("Enter Item Price: "))
        itemTaxable = True if (input("Is the item taxable (yes/no): ") == "yes") else False
        newItem = Item(itemName, itemPrice, itemTaxable)
        userReceipt.addItem(newItem)
        if not (input("Add another item (yes/no): ") == "yes"):
            break
    print(userReceipt.receiptToString())
    