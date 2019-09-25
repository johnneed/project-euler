"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from functools import reduce


def squareOfSum(num):
    sum = reduce((lambda x, y: x + y), range(1, num + 1))
    square = sum ** 2
    return square


def sumOfSquares(num):
    squares = [x ** 2 for x in range(1, num + 1)]
    sum = reduce((lambda x, y: x + y), squares)
    return sum


def go(num):
    num1 = squareOfSum(num)
    num2 = sumOfSquares(num)
    return num1 - num2

print(go(100))