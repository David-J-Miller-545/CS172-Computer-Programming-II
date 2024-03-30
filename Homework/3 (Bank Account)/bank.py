# Author: David Miller | djm545
# Date: 5/2/2023
# Filename: bank.py
# Purpose: Contains the abstract base class BankAccount which is inherited
#		   by instantiable classes Savings and Checking.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    __nextAccountNumber = 1000 # First Account Number, Static Variable
    def __init__(self, owner, balance = 0):
        self.__OWNER = owner
        self.__balance = balance
        self.__ACCOUNT_NUMBER = self.getNextAccountNumber() # Uses method to get the account number
        
    def getOwner(self): #Returns the name account owner as a string.
        return self.__OWNER
    
    def getBalance(self): #Returns the current balance in the account as float.
        return self.__balance
    
    def getAccountNumber(self): #Returns the account number as an integer.
        return self.__ACCOUNT_NUMBER
    
    def deposit(self, amount): #Takes a float as a parameter and increases the balance by that amount.
        self.__balance += amount
    
    def withdraw(self, amount): #Takes a float as a parameter and decrease the balance by that amount.
        self.__balance -= amount
    
    def __eq__(self, other): #Allows us to compare two BankAccount objects for equality. It returns a Boolean.
        eqBalance = self.__balance == other.getBalance()
        eqOwner = self.__OWNER == other.getOwner()
        eqAccNum = self.__ACCOUNT_NUMBER == other.getAccountNumber()
        # Technically eqAccNum is the only condition that matters as it is unique number per account
        return True if eqBalance and eqOwner and eqAccNum else False
    
    def __str__(self): #Returns a string representation of a generic BankAccount object in the format:
        string =  (f"Account Number: {self.__ACCOUNT_NUMBER}\n" +
                   f"Account Owner: {self.__OWNER}\n" +
                   f"Account Balance: ${self.__balance:.2f}")
        return string
    
    @staticmethod
    def getNextAccountNumber():
        num = BankAccount.__nextAccountNumber # Saves the Current Account Number
        BankAccount.__nextAccountNumber += 1 # Increments to the next Account Number
        return num # Returns the Original Account Number
    
    @abstractmethod
    def endOfMonth():
        pass

class Savings(BankAccount):
    def __init__(self, owner, balance = 0.00, interest = 3.25):
        super().__init__(owner, balance)
        self.__interestRate = interest
        
    def getInterestRate(self):
        return self.__interestRate
    
    def setInterestRate(self, newRate):
        self.__interestRate = newRate
        
    def __eq__(self, other):
        eqRate = self.__interestRate == other.getInterestRate()
        return True if super().__eq__(other) and eqRate else False
    
    def __str__(self):
        string =  (f"{super().__str__()}\n" +
                   f"Annual Interest Rate: {self.__interestRate:.2f}%")
        return string
        
    def endOfMonth(self):
        self.deposit(self.getBalance() * self.__interestRate / (12 * 100))
        # Interest rate is divided by 12 months and 100 to make it monthly and a percentage

class Checking(BankAccount):
    def __init__(self, owner, balance = 0.00):
        super().__init__(owner, balance)
        self.__transactions = 0
        
    def getTransactionsNum(self):
        return self.__transactions
    
    def deposit(self, amount):
        super().deposit(amount)
        self.__transactions += 1
        
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__transactions += 1
    
    def __eq__(self, other):
        eqTrans = self.__transactions == other.getTransactionsNum()
        return True if super().__eq__(other) and eqTrans else False
    
    def __str__(self):
        string =  (f"{super().__str__()}\n" +
                   f"Transactions this month: {self.__transactions}")
        return string
    
    def endOfMonth(self):
        if self.__transactions > 7:
            super().withdraw(5)
        self.__transactions = 0