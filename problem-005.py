"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from package1 import factoring

def isDivisible(topRange, num):
    for x in range(2, topRange + 1):
        print("\r", "Checking number:", num, end="")
        if(num % x):
            return False
    return True


def go(num):
    primes = factoring.findAllPrimesUpTo(num)
    highest = 1
    lowest = 1
    for x in range(2,num + 1):
        highest = highest * x;
    for y in primes:
        lowest = lowest * y;
    print("lowest is", lowest)
    print("highest is", highest)
    for z in range(lowest, highest + 1):
        if(isDivisible(num, z)):
            return z



answer = go(20)
print(answer)