'''
Catherine Turner
7/31/19
https://projecteuler.net/ Problem 2
'''

def fibonacciEvens(max):

    first = 1
    second = 2
    fibonacciE = [2]

    while (first + second) < max:
        current = first + second
        if (current % 2 == 0):
            fibonacciE.append(current)
        first = second
        second = current
    return sum(fibonacciE)

print(fibonacciEvens(4000000))
