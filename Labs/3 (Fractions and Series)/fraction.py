#Mark Boady and Matt Burlick
#Drexel University 2018
#Modified - 1/22/22 - A. Medlock
#CS 172 - Lab 3 Start Code

class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self, a, b):
        self.__num = a
        self.__den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.__den == 1 :
            return str(self.__num)
        else:
            return str(self.__num) + "/" + str(self.__den)
            
    #Get the Numerator
    def getNum(self):
        return self.__num
        
    #Get the Denominator
    def getDen(self):
        return self.__den
        
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.__num / self.__den
        
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.__num, self.__den)
        self.__num = self.__num // x
        self.__den = self.__den // x
        
    #Find the GCD of a and b
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    #Compare two fraction objects
    def __eq__(self,other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()
    
    
    
    #Complete these methods in lab
    def __add__(self, other):
        num = self.__den * other.getNum() + self.__num * other.getDen()
        den = self.__den * other.getDen()
        return Fraction(num, den)
        
    def __sub__(self, other):
        num = self.__num * other.getDen() - self.__den * other.getNum()
        den = self.__den * other.getDen()
        return Fraction(num, den)
        
    def __mul__(self, other):
        num = self.__num * other.getNum()
        den = self.__den * other.getDen()
        return Fraction(num, den)
         
    def __truediv__(self, other):
        num = self.__num * other.getDen()
        den = self.__den * other.getNum()
        return Fraction(num, den)
        
        
    def __pow__(self, exp):
        num = self.__num ** exp
        den = self.__den ** exp
        return Fraction(num, den)
    
    