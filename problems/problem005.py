'''
Catherine Turner
8/2/19
https://projecteuler.net/ Problem 5
'''

def divisibleCheck(target, max):
    current = max
    result = True
    while current > 0:
        if (target % current != 0):
            result = False
            break
        current -= 1
    return result

def smallestOption(max):
    current = 1
    while True:
        if divisibleCheck(current, max):
            break
        current += 1
    return current

print(smallestOption(20))
