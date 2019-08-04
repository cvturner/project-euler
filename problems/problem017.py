'''
Catherine Turner
8/4/19
https://projecteuler.net/ Problem 17
'''

uniqueNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
twoDigitNums = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def countNums(max):
    current = 1
    letterSum = 0

    # Compute letter count for numbers 1-19
    while current < 20 and current != max:
        for letter in uniqueNums[current-1]:
            letterSum += 1
        current += 1

    # Compute letter count for numbers 20-99
    while current > 19 and current < 100 and current != max:
        currentString = str(current)
        for letter in twoDigitNums[int(currentString[0])-2]:
            letterSum += 1
        if currentString[1] != "0":
            for letter in uniqueNums[int(currentString[1])-1]:
                letterSum += 1
        current += 1

    # Compute letter count for numbers 100-999
    while current > 99 and current < 1000 and current != max:
        currentString = str(current)
        for letter in uniqueNums[int(currentString[0])-1] + "hundred":
            letterSum += 1
        if currentString[1:] == "00":
            pass
        elif currentString[1] == "0" or currentString[1] == "1":
            for letter in "and" + uniqueNums[int(currentString[1:])-1]:
                letterSum += 1
        else:
            for letter in "and" + twoDigitNums[int(currentString[1])-2]:
                letterSum += 1
            if currentString[2] != "0":
                for letter in uniqueNums[int(currentString[2])-1]:
                    letterSum += 1
        current += 1

    # Compute letter count for 1000 (max for this program)
    if current == 1000:
        for letter in "one" + "thousand":
            letterSum += 1

    return letterSum

print(countNums(1000))
