'''
Catherine Turner
7/31/19
https://projecteuler.net/ Problem 3
'''

def smallestFactor(target):
    current = 2
    result = target
    while ((current < (target**(1/2) + 1))):
        if (target % current == 0):
            return current
        else:
            current += 1
    return result

def greatestPrimeFactor(target):
    n = target
    while True:
        factor = smallestFactor(n)
        if factor < n:
            n = n // factor
        else:
            return n

print(greatestPrimeFactor(600851475143))
