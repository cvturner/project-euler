'''
Catherine Turner
8/15/19
https://projecteuler.net/ Problem 36
'''

# Check if a number is a palindrome; if so, return True
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

# Find all numbers below max which are palindromic in base 10 and base 2
def findBinaryPalindromes(max):
    results = []
    for num in range(1, max):
        if testPalindrome(num) and testPalindrome(bin(num)[2:]):
            results.append(num)
    return results

# Find the sum of all numbers below one million which are palindromic in base 10 and base 2
print(sum(findBinaryPalindromes(1000000)))
