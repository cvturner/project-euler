'''
Catherine Turner
8/8/19
https://projecteuler.net/ Problem 24
'''

# Return all permutations of the targeted string in lexicographic order
def permutations(target):
    result = []

    # If target length can't be rearranged, return original string in a list
    if len(target) <= 1:
        result = [target]

    # Otherwise, use recursion to produce all possible strings and add them to results list
    else:
        for digit in target:
            options = permutations(target.replace(digit, ""))
            for option in options:
                result.append(digit + option)

    return result

# Print the millionth permutation of "0123456789" (index 1000000 - 1 in a list)
print(permutations("0123456789")[999999])
