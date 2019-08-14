'''
Catherine Turner
8/13/19
https://projecteuler.net/ Problem 34
'''

# n! = n * (n-1)! = ... (recursion)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# For every digit in a number, find its factorial. Sum those factorials and return that value.
def factorialSum(target):
    result = 0
    for digit in str(target):
        result += factorial(int(digit))
    return result

# Find all values who are equal to their own factorial sums.
def equalToFactorialSum():
    result = 0
    count = 1
    # Find the value at which the factorial sum of a number can't be equal to it
    while (factorial(9) * count) > (10 ** count):
        count += 1
    # Make the number you just found the maximum value for your range
    for num in range(3, 10**count):
        # If the number is equal to the sum of its digits' factorials, add it to the result
        if num == factorialSum(num):
            result += num
    return result

print(equalToFactorialSum())
