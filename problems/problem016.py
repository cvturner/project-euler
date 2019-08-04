'''
Catherine Turner
8/3/19
https://projecteuler.net/ Problem 16
'''

# Provide number and what power you want to raise it to
# Calculate sum of the digits in the resulting number
def powerSum(num, pow):
    power = (num ** pow)
    powSum = 0
    for x in str(power):
        powSum += int(x)
    return powSum

print(powerSum(2, 1000))
