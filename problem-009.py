"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
This algorithm could be improved by generating pythagorean triples 
 
"""



import math


def isSquare(num):
    return num != 0 and not (math.sqrt(num) % 1)


def getAandBAddends(addend):
    addends = []
    top = int(addend) ** 2
    bottom = int((addend ** 2) / 2) - 1
    for x in range(0, top):
        b = x
        a = top - x
        if (isSquare(a) and isSquare(b)) and a < b:
            addends.append((math.sqrt(a), math.sqrt(b)))
    return addends


def getSquareAddends(sum):
    addends = []
    bottom = int(sum / 2) - 2
    top = int(sum)
    for x in range(0, top):
        ab = getAandBAddends(x)
        for y in ab:
            if int(y[0] + y[1] + x) == sum:
                addends.append((int(y[0]), int(y[1]), x))
    return addends


answer = getSquareAddends(1000)[0]
print(answer)
print("a = ", answer[0], " b = ", answer[1], "c = ", answer[2])
print("product abc =", answer[0] * answer[1] * answer[2])
