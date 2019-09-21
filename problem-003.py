"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?
"""


# The Sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes.
def sieve(prime, nums):
    foo = filter((lambda x: x % prime), nums)
    return list(foo)


def generatePrimes(topRange=7500):
    nums = list(range(2, topRange + 1))
    while (len(nums) > 0):
        yield nums[0]
        nums = sieve(nums[0], nums)


def findLargestPrimeFactor(num):
    if num < 2 or num % 1:
        return 'Enter a integer larger than 1'
    prime = generatePrimes(num)
    myPrime = next(prime)
    while num > myPrime:
        if not (num % myPrime):
            num = num / myPrime
        else:
            myPrime = next(prime)
    return myPrime


print(findLargestPrimeFactor(600851475143))
