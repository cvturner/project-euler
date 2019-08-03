'''
Catherine Turner
8/3/19
https://projecteuler.net/ Problem 14
'''

# Produce the Collatz sequence using the provided starting number
# Return the length of the respective Collatz sequence
def collatzTermCount(starter):
    collatzSeq = [starter]
    current = starter
    while True:
        if current == 1:
            return len(collatzSeq)
        elif (current % 2 == 0):
            current = current / 2
            collatzSeq.append(current)
        else:
            current = 3 * current + 1
            collatzSeq.append(current)

# Find the longest Collatz sequence using starting numbers from 1 to maxStarter
# Return the starting number corresponding to the longest sequence
def longestCollatz(maxStarter):
    topLength = 0
    topLengthStarter = 0
    for num in range(1, maxStarter):
        currentLen = collatzTermCount(num)
        if currentLen > topLength:
            topLength = currentLen
            topLengthStarter = num
    return topLengthStarter

print(longestCollatz(1000000))
