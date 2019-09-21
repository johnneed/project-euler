"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largestPalindrom = 0

def isPalindrome(num):
    return str(num)[::-1] == str(num)

