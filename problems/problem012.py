'''
Catherine Turner
8/3/19
https://projecteuler.net/ Problem 12
'''

# Return how many divisors the provided target has
def divisorCount(target):
    divisorList = []
    for num in range(1, int(target**0.5 + 1)):
        if target % num == 0:
            divisorList.append(num)
            divisorList.append(target/num)
    return len(divisorList)

# Increment through the sequence of triangle numbers until the divisor count is greater than provided divCount
def triDivisors(divCount):
    triNum = 1
    count = 1
    while True:
        if divisorCount(triNum) > divCount:
            return triNum
        count += 1
        triNum += count

print(triDivisors(500))
