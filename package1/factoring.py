import math
from functools import reduce
from package1.primes import primeList

primesCache = primeList


def flatten(aList, t=None):
    if t is None:
        t = []
    for i in aList:
        if type(i) != list:
            t.append(i)
        else:
            t = flatten(i, t)
    return t


def _isPrime(num):
    for prime in primesCache:
       if not bool(num % prime):
           return False
    return True

def _findNextPrime():
    num = primesCache[-1] + 1
    while not _isPrime(num):
        print("\r","checking prime status for", num, end='')
        num += 1
    primesCache.append(num)
    return num


def generatePrimes():
    index = 0
    while (True):
        yield primesCache[index]
        index += 1
        if( index >= len(primesCache)):
            _findNextPrime()


def findAllPrimesUpTo(num):
    primeGenerator = generatePrimes()
    primes = []
    while True:
        prime = next(primeGenerator)
        if (prime > num):
            break
        primes.append(prime)
    return primes


def isPrime(num):
    primes = findAllPrimesUpTo(num)
    return _isPrime(num)


def getFirstPrimeFactor(num):
    primeGenerator = generatePrimes()
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
