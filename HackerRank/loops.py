#!/bin/python3
# https://www.hackerrank.com/challenges/python-loops

if __name__ == '__main__':
    n = int(input())
    assert 1 <= n <= 20, "n outside constraints"
    for i in range(n):
        print(i**2)
