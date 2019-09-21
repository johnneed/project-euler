"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from functools import reduce

allNumbers = range(1, 1000)

multiples = filter((lambda x: not x % 3 or not x % 5), allNumbers)

sum = reduce((lambda x, y: x + y), multiples)

print(sum)


