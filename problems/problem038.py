'''
Catherine Turner
8/17/19
https://projecteuler.net/ Problem 38
'''

# Check for repeated integers or any occurrences of 0
def checkForRepeats(target):
    targetList = list(target)
    for digit in targetList:
        if (targetList.count(digit) > 1) or digit == "0":
            return True
    return False

# Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
# with (1, 2, ..., n) where n > 1
def findPandigitalProducts():
    current = 0
    # Max n resulting in concatenation of 9 digits is 7
    for n in range(2, 8):
        # Max range of values that result in concatenation of 9 digits given the range of n
        for num in range(1, 10**(9//n)):
            result = ""
            # Concatenate result with num*n for every n in range
            for x in range(1, n+1):
                result += str(num*x)
            # If the sorted result is pandigital, set the current result to the max between the current result and
            # the sorted result.
            if "".join(sorted(result)) == "123456789":
                current = max(current, int(result))
    # Return the maximum result
    return current

# Display the result
print(findPandigitalProducts())
