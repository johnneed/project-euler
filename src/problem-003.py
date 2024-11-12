"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?
"""
from functools import reduce


def isPrime(primes, num):
    foo = reduce((lambda x, y: x and bool(num % y)), primes, True)
    return foo


def findNextPrime(primes):
    num = primes[-1] + 1
    while not isPrime(primes, num):
        num += 1
    return num


def generatePrimes(topRange):
    primes = [2]
    while (topRange >= primes[-1]):
        yield primes[-1]
        newPrime = findNextPrime(primes)
        primes.append(newPrime)


def findLargestPrimeFactor(num):
    if num < 2 or num % 1:
        raise Exception('Invalid parameter. Enter an integer larger than 1')
    prime = generatePrimes(num)
    myPrime = next(prime)
    while num > myPrime:
        if not (num % myPrime):
            num = num / myPrime
        else:
            myPrime = next(prime)
    return myPrime

print(findLargestPrimeFactor(600851475143))
