'''
Catherine Turner
8/13/19
https://projecteuler.net/ Problem 33
'''

# If numerator and denominator share a digit, remove one instance of that digit from both.
# If the fraction without those digits is the same as the original, return True and return the new numerator
# and denominator.
def cancelDigits(pair):
    num = pair[0]
    den = pair[1]
    for digit in range(1, 10):
        if str(digit) in str(num) and str(digit) in str(den):
            digit = str(digit)
            num = str(num)
            den = str(den)
            newNum = int(num.replace(str(digit), "", 1))
            newDen = int(den.replace(str(digit), "", 1))
            if newDen == 0:
                return False, None
            elif (pair[0]/pair[1]) == newNum/newDen:
                return True, [newNum, newDen]
    return False, None

# For fractions less than 1 with 2 digits in both their numerators and denominators, check which are
# "digit cancelling fractions." Find their product.
def digitCancellingFractions():
    results = []
    for den in range(10, 100):
        for num in range(10, den):
            if cancelDigits([num, den])[0]:
                results.append(cancelDigits([num, den])[1])
    productNum = 1
    productDen = 1
    for fraction in results:
        productNum *= fraction[0]
        productDen *= fraction[1]
    return [productNum, productDen]

# Simplify a fraction, provided the numerator and denominator in a list.
def simplify(target):
    num = target[0]
    den = target[1]
    for value in range(2, 10 ** min(len(str(num)), len(str(den)))):
        if (num % value == 0) and (den % value == 0):
            num = num // value
            den = den // value
    return [num, den]

# Find the simplified product result of the digit cancelling fractions function, and print its denominator.
result = simplify(digitCancellingFractions())
print(result[1])
