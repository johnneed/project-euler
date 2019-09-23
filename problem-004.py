"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from package1 import factoring

largestPalindrome = 0


def isPalindrome(num):
    numStr = str(num)
    return numStr[::-1] == numStr


def findLargestPalindrome(topRange):
    for x in range(topRange, 0, -1):
        if (isPalindrome(x)):
            return x


def findLargestIntegerOfSize(digits):
    if digits < 1 or digits % 1:
        raise Exception('Invalid input. Enter a positive Integer')
    newSum = 9 * 10 ** (digits - 1)
    return newSum if digits == 1 else newSum + findLargestIntegerOfSize(digits - 1)


def hasRightNumberOfDigits(size, num):
    if size < 1 or size % 1:
        raise Exception('Invalid input. Enter a positive Integer')
    topRange = findLargestIntegerOfSize(size)
    bottomRange = 10 ** (size - 1)
    return bottomRange <= num <= topRange


def findSizedFactors(primeFactors, size):
    arLen = len(primeFactors)
    topRange = 0
    for x in range(0, arLen):
        topRange += 2 ** x
    for mask in range(1, topRange):
        left = 1
        right = 1
        for index in range(0, arLen):
            if ((2 ** index) & mask):
                left = left * primeFactors[index]
            else:
                right = right * primeFactors[index]
        if hasRightNumberOfDigits(size, right) and hasRightNumberOfDigits(size, left):
            print("Palindrome",
                  left * right,
                  "has 2 factors with ",
                  size,
                  "digits each:",
                  left, "and", right, )
            return [left, right]
    return None


def findLargesPaldromeWithFactorSize(size):
    largestProduct = findLargestIntegerOfSize(size)
    largePalindrome = findLargestPalindrome(largestProduct ** 2)

    def findTheRightFactors(num):
        print("checking palidrome", num)
        if num < 0:
            return None
        factors3 = factoring.FactorNode(num)
        print('\nfactoring', num)
        factors2 = factors3.toList()
        print(num, 'has factors', factors2)
        factors = findSizedFactors(factors2, size);
        if factors:
            return factors[1] * factors[0]
        nextNum = findLargestPalindrome(num - 1)
        return findTheRightFactors(nextNum)

    return findTheRightFactors(largePalindrome)


foo = findLargesPaldromeWithFactorSize(3)
print(foo)
