#Name: Devyn Conaway
#Assignment: Lab 7
#Date: 3/7/2026

#Problem3.py
#Euler Problem 3

from NumberTests import isPrime
from NumberTests import getFactors

def main():
  number = int(input("Enter a number: "))
  factors = getFactors(number)
  print(factors)

  for f in factors:
     if isPrime(f):
        print(f)

if __name__ == '__main__':
    main()