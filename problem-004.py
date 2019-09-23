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
        if(isPalindrome(x)):
            return x

def findLargestIntegerOfSize(digits):
    if digits < 1 or digits % 1:
       raise Exception('Invalid input. Enter a positive Integer')
    newSum = 9 * 10 ** (digits - 1)
    return  newSum if digits == 1 else newSum + findLargestIntegerOfSize(digits - 1)


def productHasTwoGoodFactors(factors, size):
    def foo(factor, factors)
        if factor >= 10 ** size and <= findLargestIntegerOfSize(size)



def findLargesPaldromeWithFactorSize(size):
    largestProduct = findLargestIntegerOfSize(size)
    largePalindrome = findLargestPalindrome(largestProduct)
    factors = factoring.FactorNode(largePalindrome)
    factors = factors.toList()
    isGood = productHasTwoGoodFactors(factors, size);
    return isGood


foo = findLargesPaldromeWithFactorSize(3)