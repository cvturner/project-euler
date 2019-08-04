'''
Catherine Turner
8/3/19
https://projecteuler.net/ Problem 15
'''

# n! = n * (n-1)! = ... (recursion)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Combination formula: nCr = n! / r! * (n - r)!
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(combination(40, 20))
