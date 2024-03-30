# HEADER COMMENT HERE
from money import Money
import inputroutines

def menuInRange(lower, upper) :
    number = 0
    try:
        number = int(input())
        if(not(number >= lower and number <= upper)):
            print('Invalid choice. Try again.')
    except Exception as e:
        print('Invalid choice. Try again.')
    return number

if __name__ == "__main__":
    userSelection = 0
    userAccount = Money()
    while userSelection != 4:
        print("1. Deposit\n2. Withdraw\n3. See current balance\n4. Exit\nEnter your choice: ", end = '')
        userSelection = menuInRange(1,4)
        if userSelection == 1:
            print("Deposit")
            print("Enter the dollar amount: ")
            tranDollars = inputroutines.intInRange(0, 1000)
            print("Enter the cents amount: ")
            tranCents = inputroutines.intInRange(0, 99)
            userAccount.addDollars(tranDollars)
            userAccount.addCents(tranCents)
            print("Transaction completed.")
        elif userSelection == 2:
            print("Withdraw")
            print("Enter the dollar amount: ")
            tranDollars = inputroutines.intInRange(0, 1000)
            print("Enter the cents amount: ")
            tranCents = inputroutines.intInRange(0, 99)
            tranAmount = Money(tranDollars, tranCents)
            if userAccount >= tranAmount:
                userAccount = userAccount - tranAmount
                print("Transaction completed.")
            else:
                print("You do not have enough funds.")
            
        elif userSelection == 3:
            #View Balance
            print(f"Your current balance is: {userAccount}")
        elif userSelection == 4:
            print("Good-bye!")
        else:
            pass