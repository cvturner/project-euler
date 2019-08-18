'''
Catherine Turner
8/18/19
https://projecteuler.net/ Problem 39
'''

# If "target" is the perimeter of a right angle triangle with integral length sides, return all solutions
# for the side lengths of that triangle.
def pythagTriplet(target):
    results = []
    for a in range(1, target + 1):
        for b in range(a, target + 1):
            c = target - a - b
            if (a**2 + b**2 == c**2):
                result = [a, b, c]
                results.append(result)
    return results

# Return the perimeter of a right angle triangle with the most solutions for its possible side lengths
def maxPerimeter(max):
    maxP = 0
    maxSolutions = 0
    for perimeter in range(1, max+1):
        result = pythagTriplet(perimeter)
        if len(result) > maxSolutions:
            maxP = perimeter
            maxSolutions = len(result)
    return maxP

# Return the value of p <= 1000 for which the number of solutions is maximized
print(maxPerimeter(1000))
