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

def notAbundantSums(max):

    # Create list to hold values for all positive integers
    results = ['1'] * max

    # Create list of abundant numbers up to / including max
    abundants = abundantNums(max)

    # Find all potential abundant+abundant sums, and mark them in results list
    for a in abundants:
        for b in abundants:
            if (a+b) < max:
                results[a+b] = '0'
            else:
                break

    # Find the total of the remaining positive integers in the results list
    total = sum(a for (a, b) in enumerate(results) if b == '1')

    return total

print(notAbundantSums(28123))
