'''
Catherine Turner
8/11/19
https://projecteuler.net/ Problem 30
'''

# Check if the sum of a number's individual digits raised to a certain power is equal to the original number.
def checkPower(target, power):
    result = 0
    for digit in str(target):
        result += int(digit)**power
    if target == result:
        return True
    else:
        return False

# For provided power, find the sum of the numbers for which the sum of their individual digits raised to the provided
# power is equal to the original number.
def findPowerSum(power):
    result = 0
    for num in range(2, findPowerSumLimit(power)):
        if checkPower(num, power):
            result += num
    return result

# Max is found when number hits i digits and i*9^power < 10^i (no longer possible)
def findPowerSumLimit(power):
    i = 1
    while ((i*9**power) > 10**i):
        i += 1
    return 10**i

print(findPowerSum(5))
