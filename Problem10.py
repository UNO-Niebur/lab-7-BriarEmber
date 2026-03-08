#Problem7.py
#Euler Problem 10
#The sum of primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all primes below 2,000,000

from NumberTests import addPrimes


def main():
    number = int(input("Enter a number: "))
    total = addPrimes(number)
    print(total)



if __name__ == '__main__':
    main()