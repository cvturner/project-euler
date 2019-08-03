'''
Catherine Turner
8/3/19
https://projecteuler.net/ Problem 10
'''

def checkPrime(num):
    result = True
    if num == 2:
        return result
    for x in range(2, int(num**0.5 + 1)):
        if num % x == 0:
            result = False
            break
    return result

def primeSum(max):
    primes = []
    current = 1

    while current < (max-1):
        current += 1
        if checkPrime(current):
            primes.append(current)

    return sum(primes)

print(primeSum(2000000))
