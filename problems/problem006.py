'''
Catherine Turner
8/2/19
https://projecteuler.net/ Problem 6
'''

def sumOfSquares(max):
    result = sum(x**2 for x in range(1, max + 1))
    return result

def squareOfSums(max):
    result = (sum(x for x in range(1, max + 1)))**2
    return result

print(squareOfSums(100) - sumOfSquares(100))
