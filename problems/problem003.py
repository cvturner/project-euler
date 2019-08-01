'''
Catherine Turner
7/31/19
https://projecteuler.net/ Problem 3
'''

import math

def smallestFactor(target):
    current = 2
    result = target
    while ((current < (math.sqrt(target) + 1))):
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
