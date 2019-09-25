"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from package1 import factoring
from functools import reduce

def isDivisible(topRange, num):
    for x in range(2, topRange + 1):
        print("\r", "Checking number:", num, end="")
        if (num % x):
            return False
    return True


def cleanFactor(lists, factor):
    newLists = []
    for x in lists:
        cleaned = (x[:x.index(factor):] + x[x.index(factor) + 1::]) if factor in x else x
        newLists.append(cleaned)
    return newLists


def sieve(factorsList, factors=None):
    if factors == None:
        factors = []
    filteredLists = list(filter((lambda l: len(l)), factorsList))
    if not len(filteredLists):
        return factors
    bar = filteredLists[0][0]
    newFactors = factors.copy()
    newFactors.append(bar)
    cleaned = cleanFactor(filteredLists, bar)
    return sieve(cleaned, newFactors)


def go(num):
    factoredNumbers = []
    for x in range(2, num + 1):
        factoredNumbers.append(factoring.FactorNode(x).toList())
    finalFactors =  sieve(factoredNumbers)
    answer = reduce((lambda x, y: x * y), finalFactors)
    return answer

answer = go(20)
print(answer)
