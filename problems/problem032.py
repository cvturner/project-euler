'''
Catherine Turner
8/12/19
https://projecteuler.net/ Problem 32
'''

# Return a list of the target's divisors, in pairs
def divisors(target):
    divisorPairs = []
    for num in range(1, int(target**0.5 + 1)):
        if target % num == 0:
            pair = [num, target//num]
            divisorPairs.append(pair)
    return divisorPairs

# Find products whose identities, containing multiplicand, multiplier, and product, are 1-9 pandigital
def findPandigital():
    products = []
    # Use divisors function to create a sorted string of a product, its multiplicand, and multiplier, and check if
    # it is equal to "123456789" and thus 1-9 pandigital. If so, add the product to the products list.
    for num in range(1, 10000):
        for pair in divisors(num):
            pandigital = str(num) + str(pair[0]) + str(pair[1])
            if "".join(sorted(pandigital)) == "123456789":
                products.append(num)
    # Remove any repeats in the list
    for num in products:
        while products.count(num) > 1:
            products.remove(num)
    return products

# Find the sum of all products that fit the above rule
print(sum(findPandigital()))
