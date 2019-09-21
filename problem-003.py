"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Sieve of Eratosthenes
In mathematics, the sieve of Eratosthenes, one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.

The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime. This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime.
"""

primes = [];

""" sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes.
The function "sieve" takes two parameters
 prime: any prime number
 nums: a list of integers in sequential order.
the function should return a list of all numbers in n  not evenly divisble by prime;
for instance : sieve(2, [2,3,6,15]) would return [3,15]
"""

def sieve(prime, nums):
    print(prime)
    foo = filter((lambda x: x % prime), nums)
    return list(foo)

def findPrimes(primes, nums):
    primeCandidates = sieve(primes[len(primes) - 1], nums)
    if len(primeCandidates) == 0:
        return
    newPrimes = primes + [primeCandidates[0]]
    findPrimes(newPrimes, primeCandidates)

# 7500 gives find the biggest number of primes without a max recursion depth error.
findPrimes([2], list(range(2, 7500)))
