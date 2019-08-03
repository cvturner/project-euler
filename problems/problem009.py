'''
Catherine Turner
8/2/19
https://projecteuler.net/ Problem 9
'''

def pythagTriplet(target):
    result = None
    for a in range(1, target + 1):
        for b in range(a, target + 1):
            c = target - a - b
            if (a**2 + b**2 == c**2):
                result = (a * b * c)
    return result

target = 1000
print(pythagTriplet(target))
