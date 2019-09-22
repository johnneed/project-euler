from functools import reduce


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
    primeGenerator = generatePrimes(num)
    primes = []
    while True:
        prime = next(primeGenerator)
        if(prime > num):
            break
        primes.append(prime)
    return primes

def isPrime(num):
    primes = findAllPrimesUpTo(num)
    return _isPrime(primes, num)

class factorNode:
    def __init__(self,primeFactor, childNode):
        self.primeFactor = primeFactor
        self.childNode = childNode

