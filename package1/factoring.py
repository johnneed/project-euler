import math
import cmath
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
    print("\r", "Finding Primes", end='')
    num = primesCache[-1] + 2
    while not _isPrime(num):
        num += 2

    primesCache.append(num)
    return num


def generatePrimes():
    index = 0
    while (True):
        yield primesCache[index]
        index += 1
        if (index >= len(primesCache)):
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
    if num == 1:
        return 1
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


def solveQuadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (sol1, sol2)


def sieveAllPrimesUpTo(num):
    primelist = [2]
    arraySize = primelist[-1] if primelist[-1] < 1000 else 1000
    startingIndex = primelist[-1]
    finalIndex = startingIndex + arraySize
    while finalIndex < num + arraySize:
        currentBlock = set(range(startingIndex, finalIndex))
        for x in primelist:
            currentList = list(currentBlock)
            for y in currentList:
                if (y % x == 0):
                    currentBlock.remove(y)
        primelist += currentBlock
        arraySize = primelist[-1] if primelist[-1] < 1000 else 1000
        startingIndex = finalIndex + 1
        finalIndex += arraySize
        print("\r", primelist, end='')
    print("\n")
    return primelist


def findAllFactors(primeFactors):
    factor1 = primeFactors[0]
    otherFactors = primeFactors[1:]
    if len(otherFactors) == 0:
        return [1, factor1]
    factors = findAllFactors(otherFactors)
    return factors + list(map(lambda x: factor1 * x, factors))