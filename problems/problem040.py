'''
Catherine Turner
8/19/19
https://projecteuler.net/ Problem 40
'''

# Create an irrational decimal fraction by concatenating positive integers up to "count"
def positiveFraction(count):
    fraction = "0."
    for num in range(1, count + 1):
        fraction += str(num)
    return fraction

# Return the nth digit of a decimal, excluding the preceding "0."
def findDecimalDigit(decimal, n):
    fraction = str(decimal)[2:]
    return fraction[n-1]

# Using the result of the positiveFraction function, find the product of the 10**1, 10**2, ..., 10**7 of its
# fractional part.
def champernowneConstant():
    fraction = positiveFraction(1000000)
    result = 1
    for num in range(1, 7):
        result = result * int(findDecimalDigit(fraction, 10**num))
    return result

# Execute the above function.
print(champernowneConstant())
