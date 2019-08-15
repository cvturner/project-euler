'''
Catherine Turner
8/14/19
https://projecteuler.net/ Problem 35
'''

# Return the rotation of the target integer for the appropriate iteration
# If iteration = 0, then the target itself is returned
def rotate(target, iteration):
    target = str(target)
    length = len(target)
    result = target[iteration:length] + target[0:iteration]
    return int(result)

# Check if num is prime; if so, return True
def checkPrime(num):
    result = True
    if num == 2:
        return result
    for x in range(2, int(num**0.5 + 1)):
        if num % x == 0:
            result = False
            break
    return result

# Find all circular primes below a provided maximum integer
def circularPrimes(max):
    results = []
    for num in range(2, max):
        result = True
        x = 0
        # Check all possible rotations of the integer for primeness
        while x < len(str(num)):
            if not checkPrime(rotate(num, x)):
                result = False
                break
            x += 1
        # If all rotations of the integer are prime, add that integer to the results list
        if result:
            results.append(num)
    return results

# Display how many circular primes there are below one million
print(len(circularPrimes(1000000)))
