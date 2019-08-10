'''
Catherine Turner
8/9/19
https://projecteuler.net/ Problem 27
'''

# Check if absolute value of num is prime; if so, return True
def checkPrime(num):
    num = abs(num)
    result = True
    if num == 2:
        return result
    for x in range(2, int(num**0.5 + 1)):
        if num % x == 0:
            result = False
            break
    return result

# Generate quadratic formulas of the form n^2 + an + b within the -aMax to aMax and -bMax - 1 to bMax + 1
# For each formula, count the number of primes generated for consecutive values of n
# Return the values of a and b for the formula with the greatest consecutive number of prime results
def checkQuadPrimes(aMax, bMax):
    aResult = None
    bResult = None
    maxCount = 0

    for a in range(-aMax, aMax):
        for b in range(-bMax - 1, bMax + 1):
            n = 0
            while (checkPrime(n**2 + a*n + b)):
                n += 1
            if n > maxCount:
                maxCount = n
                aResult = a
                bResult = b

    return [aResult, bResult]

# Save the result of the checkQuadPrimes function and print the product of aResult * bResult
resultList = checkQuadPrimes(1000, 1000)
print(resultList[0] * resultList[1])
