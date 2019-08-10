'''
Catherine Turner
8/10/19
https://projecteuler.net/ Problem 28
'''

# Generate a square of dimension x dimension that contains a spiral, starting from 1 and incrementing by 1,
# from the center of the square.
def genSpiral(dimension):

    # Create empty lists of fitting dimensions
    spiral = []
    for y in range(dimension):
        spiral.append([])
        for x in range(dimension):
            spiral[y].append(0)

    # Initialize the spiral with its center value
    a = 1
    value = 1
    currentX = dimension//2
    currentY = dimension//2
    (spiral[currentY])[currentX] = value
    value += 1

    # Begin to create the spiral
    while a < dimension:
        if (a%2 != 0):
            for b in range(a):
                (spiral[currentY])[currentX+b+1] = value
                value += 1
            currentX += a
            for b in range(a):
                (spiral[currentY+b+1])[currentX] = value
                value += 1
            currentY += a

        else:
            for b in range(a):
                (spiral[currentY])[currentX-b-1] = value
                value += 1
            currentX -= a
            for b in range(a):
                (spiral[currentY-b-1])[currentX] = value
                value += 1
            currentY -= a

        a += 1

    # When a == dimension, we have to complete the top row of the spiral
    if a == dimension:
        i = 1
        while i < dimension:
            (spiral[currentY])[currentX+i] = value
            i += 1
            value += 1

    # Return the final result
    return spiral

# Find the sum of the numbers on the diagonals of a square made of lists
def diagSum(target):
    dimension = len(target)
    result = 0

    # Add diagonal values to result
    for y in range(dimension):
        result += target[y][y] + target[y][dimension-1-y]

    # Subtract 1 from result to account for duplication of the center value of the square
    return (result-1)

# Print the sum of all diagonal values in a 1001 x 1001 spiral
print(diagSum(genSpiral(1001)))
