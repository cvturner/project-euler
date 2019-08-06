'''
Catherine Turner
8/6/19
https://projecteuler.net/ Problem 20
'''

# n! = n * (n-1)! = ... (recursion)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Return the sum of a number's individual digits (i.e. given 123, returns 1 + 2 + 3 or 6)
def digitSum(target):
    targetStr = str(target)
    return sum(int(digit) for digit in targetStr)

# Find 100! then print the sum of its digits
print(digitSum(factorial(100)))
