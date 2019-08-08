'''
Catherine Turner
8/7/19
https://projecteuler.net/ Problem 23
'''

# Return a target's proper divisors
def properDivisors(target):
    divisorList = []
    for num in range(1, int(target**0.5 + 1)):
        if target % num == 0:
            divisorList.append(num)
            if (divisorList.count(target/num) == 0) and (int(target/num) != target):
                divisorList.append(int(target/num))
    divisorList.sort()
    return divisorList

# Generate a list of abundant numbers less than the maximum
def abundantNums(max):
    abundants = []

    for num in range(2, max + 1):
        if sum(properDivisors(num)) > num:
            abundants.append(num)

    return abundants

# Generate a list of positive integers up to provided max that can't be calculated by adding two abundant numbers
def notAbundantSums(max):

    # Create a list holding all positive integers from 1 to the max
    results = list(range(1, max))

    # Create list of abundant numbers up to / including max
    abundants = abundantNums(max)

    # Remove abundant + abundant sums from positive integers list
    for a in abundants:
        for b in abundants:
            if (a+b) < max:
                results[a+b-1] = 0
            else:
                break
    while results.count(0) != 0:
        results.remove(0)

    return results

# Find the sum of all positive integers up to 28123 that can't be calculated by adding two abundant numbers
print(sum(notAbundantSums(28123)))
