'''
Catherine Turner
8/16/19
https://projecteuler.net/ Problem 37
'''

# Check if num is prime; if so, return True
def checkPrime(num):
    result = True
    if num == 1:
        return False
    if num == 2:
        return result
    for x in range(2, int(num**0.5 + 1)):
        if num % x == 0:
            result = False
            break
    return result

# Find a provided number (i.e. count = 7, find 7) of primes that are both truncatable from left to right and right
# to left. Return a list of those primes.
def truncatablePrimes(count):
    results = []
    num = 10
    # Max count is 11
    while len(results) < count or len(results) < 11:
        prime = True
        x = 0
        while x < len(str(num)):
            current1 = str(num)[x:]
            current2 = str(num)[0:len(str(num))-x]
            if (not checkPrime(int(current1))) or (not checkPrime(int(current2))):
                prime = False
                break
            x += 1
        if prime == True:
            results.append(num)
        num += 1
    return results

# Find the sum of the only eleven primes that are truncatable from right to left and left to right.
print(sum(truncatablePrimes(11)))
