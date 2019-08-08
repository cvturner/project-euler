'''
Catherine Turner
8/8/19
https://projecteuler.net/ Problem 26
'''

# Return the length of the recurring cycle for fraction with provided denominator
def recurringLength(denom):

    covered = [] # List for digits in recurring cycle we've covered
    count = 1
    current = 1 # Begin with numerator set to 1

    # Use long division until we cycle back to where we began
    while True:
        count += 1 # Increment when new number is covered
        if current in covered:
            return count - 1
        else:
            covered.append(current) # Add new digit to list
            current = current*10 % denom

# Find the number x < 1000 for which 1/x contains the longest recurring cycle in its decimal fraction part
print(max(recurringLength(x) for x in range(1, 999)))
