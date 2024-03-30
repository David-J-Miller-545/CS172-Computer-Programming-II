# Author: David Miller | djm545
# Date: 5/2/2023
# Purpose: This Program is a simulation of the operations of a very simple bank.

from bank import Savings, Checking

# Just an input validation method that serves as a menu selection
# Inputing a string to print, a lower number bound, and an upper number bound
def menuSelect(lower, upper, menu) :
    number = 0
    while True:
        try:
            print(menu)
            number = int(input())
            while(not(number >= lower and number <= upper)): # Runs until the number is in range
                print('Invalid choice. Try again.')
                print(menu)
                number = int(input())
            break
        except Exception as e:
            print('Invalid choice. Try again.')
    return number
        
# Input Validation that takes a variable type as input to give a more accurate error message
def numInput(varType):
    number = -1 # -1 because all negative values are out of range
    while True:
        try:
            number = float(input()) # Uses a float because any float can be casted as an int
            while(not(number >= 0)): # Runs until the number is greater than 0
                number = float(input())
                print('Enter a greater than or equal to zero: ')
            break
        except Exception as e:
            print(f'Invalid input: an {varType} value was expected. Try again: ')
            # varType is used in the error message
    return number

def createAccount():
    #inputs = (str(Owner's Name), float(Balance))
    name = input("Enter owner's name: ")
    print("Enter initial balance: ", end="")
    inputs = (name, numInput("float")) # Returns a tuple that contains (name, balance)
    return inputs

def searchForAccount(accountNum, accounts):
    for a in accounts: # For every Account
        if a.getAccountNumber() == accountNum: # If the Account Numbers are equal
            return a # Return the Account
    return None # If no accounts are returned, return nothing

if __name__ == "__main__":
    bankAccounts = []
    menu = ("1. Create Savings Account\n" +
            "2. Create Checking Account\n" +
            "3. Deposit\n" +
            "4. Withdraw\n"+
            "5. Perform End of Month Operations\n" +
            "6. Display Savings Accounts\n" +
            "7. Display Checking Accounts\n"+
            "8. Display All Accounts\n" +
            "9. Exit\n" +
            "Enter your choice: ")
    while True:
        selection = menuSelect(1, 9, menu)
        
        # MENU
        if selection == 1: # 1. Create Savings
            print("Savings Account")
            accountDetails = createAccount() # Returns the tuple (name, balance)
            bankAccounts.append(Savings(accountDetails[0], accountDetails[1]))
            print("Account added")
            
        elif selection == 2: # 2. Create Checking
            print("Checking Account")
            accountDetails = createAccount() # Returns the tuple (name, balance)
            bankAccounts.append(Checking(accountDetails[0], accountDetails[1]))
            print("Account added")
            
        elif selection == 3: # 3. Deposit
            print("Deposit")
            print("Enter account number: ")
            account = searchForAccount(int(numInput("integer")), bankAccounts)
                                    #  int(numInput("integer")) casts the returned float to an int
            # If it is an instance of Bank Account but Bank Account wasn't imported
            if isinstance(account, Savings) or isinstance(account, Checking):
                print("Enter amount to deposit:")
                transAmount = numInput("float")
                account.deposit(transAmount)
            else:
                print("That account number does not exist")
                
        elif selection == 4: # 4. Withdraw
            print("Withdraw")
            print("Enter account number: ")
            account = searchForAccount(int(numInput("integer")), bankAccounts)
                                    #  int(numInput("integer")) casts the returned float to an int
            # If it is an instance of Bank Account but Bank Account wasn't imported
            if isinstance(account, Savings) or isinstance(account, Checking):
                print("Enter amount to withdraw: ")
                transAmount = numInput("float")
                # If the account has enough withdraw the amount. Else, print there are not enough funds
                account.withdraw(transAmount) if transAmount <= account.getBalance() else print("You do not have enough funds")
            else:
                print("That account number does not exist")
                
        elif selection == 5: # 5. End of Month
            print("End of month operations have been performed")
            for a in bankAccounts: # For every Account
                a.endOfMonth() # Peform end of month operations
                
        elif selection == 6: # 6. Display Savings
            for a in bankAccounts: # For every Account
                if isinstance(a, Savings): # If account is a Savings Account
                    print(a) # Print the Account
                    
        elif selection == 7: # 7. Display Checkings
            for a in bankAccounts: # For every Account
                if isinstance(a, Checking): # If account is a Checking Account
                    print(a) # Print the Account
                    
        elif selection == 8: # 8. Display All
            for a in bankAccounts: # For every Account
                print(a) # Print the Account
                
        else: # 9. Exit
            print("Good-Bye!")
            break



