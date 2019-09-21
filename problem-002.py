"""
Even Fibonacci numbers

Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def findFibSum(sum, x1, x2):
    fib = x1 + x2
    if (fib > 4000000):
        return sum
    if not fib % 2:
        sum += fib
    return findFibSum(sum, x2, fib)


print(findFibSum(0, 0, 1))