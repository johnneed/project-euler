"""
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import sys
from package1 import factoring


def findSumOfAllPrimesBelow(num):
    generator = factoring.generatePrimes()
    prime = next(generator)
    sum = 0
    while (prime < num:
        sum += prime
        prime = next(generator)
    return sum

answer = findSumOfAllPrimesBelow(6)
print (answer)


if __name__ == "__main__":
    answer = findSumOfAllPrimesBelow(sys.argv[1:])
    print("\nSum all all primes below ", sys.argv[1:], "is", answer)
