'''
Catherine Turner
8/2/19
https://projecteuler.net/ Problem 7
'''

def checkPrime(num):
    result = True
    if num <= 2:
        return result
    for x in range(2, int(num**0.5 + 1)):
        if num % x == 0:
            result = False
            break
    return result

def primeList(count):
    primes = []
    current = 1

    while len(primes) < count:
        current += 1
        if checkPrime(current):
            primes.append(current)

    return primes[count-1]

print(primeList(10001))
