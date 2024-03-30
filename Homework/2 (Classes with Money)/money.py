#File Name:   money.py
# add purpose of this file here
# add your name and date here
class Money():
    def __init__(self, dollars = 0, cents = 0):
        self.__dollars = dollars
        self.__cents = cents
    
    def addDollars(self, dollars):
        self.__dollars += dollars
    
    def addCents(self, cents):
        self.__cents += cents
        if self.__cents > 100:
            self.__cents -= 100
            self.__dollars += 1
        
    def getDollars(self):
        return self.__dollars
    
    def getCents(self):
        return self.__cents
        
    def __add__(self, other):
        sumDollars = self.__dollars + other.getDollars()
        sumCents = self.__cents + other.getCents()
        if sumCents > 100:
            sumCents -= 100
            sumDollars += 1
        return Money(sumDollars, sumCents)
        
    def __sub__(self, other):
        diffDollars = abs(self.__dollars - other.getDollars())
        diffCents = self.__cents - other.getCents()
        if diffCents < 0 or self.__dollars < other.getDollars():
            diffCents += 100
            diffDollars -= 1
        return Money(diffDollars, diffCents)
        
    def __mul__(self, num):
        multDollars = self.__dollars * num
        multCents = self.__cents * num
        while multCents > 100:
            multCents -= 100
            multDollars += 1
        return Money(multDollars, multCents)
    
    def __lt__(self, other):
        if self.__dollars < other.getDollars():
            return True
        elif (self.__dollars == other.getDollars()) and (self.__cents < other.getCents()):
            return True
        else:
            return False
    
    def __le__(self, other):
        if (self.__dollars <= other.getDollars()) and (self.__cents <= other.getCents()):
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.__dollars > other.getDollars():
            return True
        elif (self.__dollars == other.getDollars()) and (self.__cents > other.getCents()):
            return True
        else:
            return False
            
    def __ge__(self, other):
        if (self.__dollars >= other.getDollars()) or ((self.__dollars >= other.getDollars()) and (self.__cents >= other.getCents())):
            return True
        else:
            return False
    
    def __eq__(self, other):
        return (self.__dollars == other.getDollars() and self.__cents == other.getCents())
    
    def __ne__(self, other):
        return not(self.__dollars == other.getDollars() and self.__cents == other.getCents())

    def __getitem__(self, index):
        if index == 0:
            return self.__dollars
        elif index == 1:
            return self.__cents
        else:
            raise IndexError("Sorry, no numbers below zero")
    
    def __str__(self):
        return f"${self.__dollars}.{self.__cents:0>2}"
        