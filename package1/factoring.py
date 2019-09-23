import math
from functools import reduce

def flatten(aList, t=[]):
    for i in aList:
        if type(i) != list:
            t.append(i)
        else:
            t = flatten(i, t)
    return t


def _isPrime(primes, num):
    return reduce((lambda x, y: x and bool(num % y)), primes, True)


def _findNextPrime(primes):
    num = primes[len(primes) - 1] + 1
    while not _isPrime(primes, num):
        num += 1
    return num


def generatePrimes(topRange):
    primes = [2]
    while (topRange >= primes[len(primes) - 1]):
        yield primes[len(primes) - 1]
        newPrime = _findNextPrime(primes)
        primes.append(newPrime)


def findAllPrimesUpTo(num):
    primeGenerator = generatePrimes(math.inf)
    primes = []
    while True:
        prime = next(primeGenerator)
        if (prime > num):
            break
        primes.append(prime)
    return primes


def isPrime(num):
    primes = findAllPrimesUpTo(num)
    return _isPrime(primes, num)


def getFirstPrimeFactor(num):
    primeGenerator = generatePrimes(num)
    prime = next(primeGenerator)
    while num % prime:
        prime = next(primeGenerator)
    return prime


def getLargestPrimeFactor(num):
    primes = findAllPrimesUpTo(num)
    return primes[-1]


class FactorNode:
    def __init__(self, product):
        primeFactor = getFirstPrimeFactor(product)
        otherFactor = int(product / primeFactor)
        self.primeFactor = primeFactor
        self.childNode = otherFactor if isPrime(otherFactor) else FactorNode(otherFactor)

    def toList(self):
        def getList(self):
            otherIsInt = type(self.childNode) is int
            otherFactor = self.childNode if otherIsInt else getList(self.childNode)
            newList = [otherFactor] + [self.primeFactor]
            return newList

        myList = getList(self)
        flattened = flatten(myList)
        filtered = filter((lambda x: x != 1), flattened)
        aList = list(filtered)
        return aList
