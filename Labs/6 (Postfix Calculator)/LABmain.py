# Author: David Miller | djm545
# Date: 5/17/23
# Purpose: An experiment with the Stack data structure by making a Postfix Calculator

from stackclass import Stack

def postfix(exp):
    exp = exp.split()
    numStack = Stack()
    result = 0
    
    for x in exp: # For each input
            try: # Check if its a number
                numStack.push(float(x)) # Push it to the number stack if a number
            except: # Its not a number
                if x == "+" or x == "-" or x == "*" or x == "/": # Check for operators
                    num2 = numStack.pop() # Right Operand
                    num1 = numStack.pop() # Left Operand
                        
                    if x == "+":
                        result = num1 + num2
                    elif x == "-":
                        result = num1 - num2
                    elif x == "*":
                        result = num1 * num2
                    elif x == "/":
                        result = num1 / num2
                    numStack.push(result)
    
    return numStack.pop()

if __name__ == "__main__":
    print("Welcome to Postfix Calculator\nEnter exit to quit")
    run = True # Run variable
    while run:
        userInput = input("Enter Expression\n") # Break up the user input into a list of each input
        if userInput == "exit": # Check for exit
            run = False # Stop the running while loop
        else:
            result = postfix(userInput)
        
        if run: # So it doesn't print the result when exiting
            print(f"Result: {result}") # Prints the most recent entry of the stack which should be the result 
        
