# Author: David Miller | djm545
# Date: 5/17/23
# Purpose: An experiment with the Stack data structure by making a Postfix Calculator

from stackclass import Stack
stack = Stack() # Global Instance of Stack

def postfix(exp):
    if not stack.isEmpty() == None:
        num2 = stack.pop() # Right Operand
        num1 = stack.pop() # Left Operand
        result = 0

        if exp == "+":
            result = num1 + num2
        elif exp == "-":
            result = num1 - num2
        elif exp == "*":
            result = num1 * num2
        elif exp == "/":
            result = num1 / num2
            
        return result

if __name__ == "__main__":
    print("Welcome to Postfix Calculator\nEnter exit to quit")
    run = True # Run variable
    while run:
        userInput = input("Enter Expression\n").split() # Break up the user input into a list of each input
        for x in userInput: # For each input
            try: # Check if its a number
                stack.push(float(x)) # Push it to the stack if a number
            except: # Its not a number
                if x == "+" or x == "-" or x == "*" or x == "/": # Check for operators
                    stack.push(postfix(x)) # Push the calculation
                elif x == "exit": # Check for exit
                    run = False # Stop the running while loop
        if run: # So it doesn't print the result when exiting
            print(f"Result: {stack.pop()}") # Prints the most recent entry of the stack which should be the result 
        