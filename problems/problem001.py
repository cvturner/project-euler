'''
Catherine Turner
7/31/19
https://projecteuler.net/ Problem 1
'''

def multipleSum(a, b, max):
    current = 1
    sum = 0
    while current < max:
        if ((current % a == 0) or (current % b == 0)):
            sum += current
        current += 1
    return sum

print(multipleSum(3, 5, 1000))
