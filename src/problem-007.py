"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
from package1 import factoring


def findNthPrime(nth):
    generator = factoring.generatePrimes()
    nthPrime = 2
    for x in range(1, nth + 1):
        nthPrime = next(generator)
    return nthPrime


print("\n\r answer is:", findNthPrime(10001))
