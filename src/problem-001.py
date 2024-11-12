"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


from functools import reduce

def multiples_of_3_and_5(lower_bound=1, upper_bound=1000):
    allNumbers = range(lower_bound, upper_bound)
    multiples = filter((lambda x: not x % 3 or not x % 5), allNumbers)
    sum = reduce((lambda x, y: x + y), multiples)
    return sum

if __name__ == "__main__":
    print(multiples_of_3_and_5(1,1000))
