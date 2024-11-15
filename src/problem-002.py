"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def find_fib_sum(upper_boundary, sum, x1, x2):
    fib = x1 + x2
    if (fib > upper_boundary):
        return sum
    if not fib % 2:
        sum += fib
    return find_fib_sum(upper_boundary, sum, x2, fib)


def even_fibonacci_numbers(upper_boundary):
    return find_fib_sum(upper_boundary, 0, 0, 1)


if __name__ == "__main__":
    print(even_fibonacci_numbers(4000000))
