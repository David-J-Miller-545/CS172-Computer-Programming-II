# Author: David Miller | djm545
# Date: 4/19/2023
# Purpose: 	Asks the user for the number of iterations and then presents the user
# 			with the final summation of a Harmonic Series, a Geometric Series of r = 1/2,
#			the same Geometric Series subtracted from 2, and finally a Partial Riemann Zeta
#			all with the same number of iterations that the user inputed.

from fraction import Fraction

def H(n):
    summation = Fraction(1, 1) # First term
    for k in range (2, n + 1): # The summation starting from second index
        term = Fraction(1, k)
        summation = summation + term
    return summation
    
def T(n):
    summation = term = Fraction(1, 2) ** 0 # First term
    for k in range (1, n + 1): # The summation starting from second index
        term = Fraction(1, 2) ** k
        summation = summation + term
    return summation
    
def Z(n):
    return Fraction(2, 1) - T(n) # 2/1 = 2
    
def R(n,b):
    summation = Fraction(1, 1) ** b # First term
    for k in range (2, n + 1): # The summation starting from second index
        term = Fraction(1, k) ** b
        summation = summation + term
    return summation
    

if __name__ == "__main__":
    #TODO
    print("Welcome to Fun with Fractions!")
    while True:
        try:
            iterations = int(input("Enter Number of iterations (integer>0):\n"))
            break
        except:
            print("Bad Input")
    harmonic = H(iterations)
    two = T(iterations)
    zero = Z(iterations)
    prz = R(iterations, iterations)
    # Print Statement below does getNum()/getDen() in order to retrieve the num and den and get the actual decimal value of the fraction.
    print(f"H({iterations})={harmonic}\n" +
          f"H({iterations})~={harmonic.getNum()/harmonic.getDen():.8f}\n" +
          f"T({iterations})={two}\n" +
          f"T({iterations})~={two.getNum()/two.getDen():.8f}\n" +
          f"Z({iterations})={zero}\n" +
          f"Z({iterations})~={zero.getNum()/zero.getDen():.8f}\n" +
          f"R({iterations},{iterations})={prz}\n" +
          f"R({iterations},{iterations})~={prz.getNum()/prz.getDen():.8f}")
