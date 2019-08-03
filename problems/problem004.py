'''
Catherine Turner
8/2/19
https://projecteuler.net/ Problem 4
'''

def testPalindrome(target):
    targetString = str(target)
    length = len(targetString)
    result = True
    current = 0
    for digit in targetString:
        if not(digit == targetString[length-1-current]):
            result = False
        current += 1
    return result

def productPalindrome(max):
    while True:
        num1 = max
        result = 0
        while num1 > (max/10):
            num2 = max
            while num2 > (max/10):
                if ((testPalindrome(num1 * num2)) and ((num1 * num2) > result)):
                    result = num1 * num2
                num2 = num2 - 1
            num1 = num1 - 1
        break
    return result

print(productPalindrome(999))
