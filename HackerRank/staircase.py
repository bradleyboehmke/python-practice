#!/bin/python3
# https://www.hackerrank.com/challenges/staircase

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, (n+1)):
        if i != n:
            spaces = ' ' * (n-i)
            hashes = '#' * i
            step = spaces + hashes
            print(step)
        else:
            print('#' * n)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
