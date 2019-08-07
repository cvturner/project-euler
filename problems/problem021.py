'''
Catherine Turner
8/6/19
https://projecteuler.net/ Problem 21
'''

# Return a target's proper divisors
def properDivisors(target):
    divisorList = []
    for num in range(1, int(target**0.5 + 1)):
        if target % num == 0:
            divisorList.append(num)
            if (int(target/num) != target):
                divisorList.append(int(target/num))
    divisorList.sort()
    return divisorList

# Check if a number is amicable
def checkAmicable(target):
    pair = sum(properDivisors(target))
    if pair != target:
        if sum(properDivisors(pair)) == target:
            return True
    else:
        return False

# Find all amicable numbers under a provided maximum
def amicableUnderMax(max):
    amicables = []

    for num in range(2, max):
        if checkAmicable(num) and (amicables.count(num) == 0):
            amicables.append(num)

    return amicables

print(sum(amicableUnderMax(10000)))
