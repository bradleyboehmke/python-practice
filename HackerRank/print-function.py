#!/bin/python3
# https://www.hackerrank.com/challenges/python-print

if __name__ == '__main__':
    n = int(input())
    result = [str(i) for i in range(1, n+1)]
    print(''.join(result))
