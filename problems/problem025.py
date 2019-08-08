'''
Catherine Turner
8/8/19
https://projecteuler.net/ Problem 25
'''

# Generates fibonacci sequence until a number with target amount of digits is reached
# Returns the index of that number in the overall sequence
def fibonacciDigits(target):

    first = 1
    second = 1
    fibonacci = [1, 1]

    if target == 1:
        return 1
    else:
        while True:
            current = first + second
            fibonacci.append(current)
            # If current is a number with target amount of digits, stop generating sequence
            if current // (10**(target-1)) >= 1:
                break
            first = second
            second = current

    return fibonacci.index(current) + 1

print(fibonacciDigits(1000))
