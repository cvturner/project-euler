'''
Catherine Turner
8/7/19
https://projecteuler.net/ Problem 22
'''

# Create list of names, sorted in alphabetical order, from provided text file
def nameList(fileName):
    nameList = []

    with open(fileName, "r") as inFile:
        for string in inFile:
            nameList = string.split("\"")

    # Remove commas and quotation marks
    for item in nameList:
        if len(item) < 2:
            nameList.remove(item)

    nameList.sort()
    return nameList

# Return a list including the "alphabetical value" of every name in the provided list
def alphabeticalValue(nameList):
    valueList = []

    # Find every character's place in the alphabet, then multiply total by name's place in the list
    for name in nameList:
        charTotal = 0
        for c in name:
            charTotal += ord(c) - ord('A') + 1
        total = (nameList.index(name) + 1) * charTotal
        valueList.append(total)

    return valueList

print(sum(alphabeticalValue(nameList("names.txt"))))
