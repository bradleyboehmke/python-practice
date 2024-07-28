#!/bin/python3
# https://www.hackerrank.com/challenges/python-tuples
# Note: This solution fails on HackerRank when using Python3 because
# hash() produces different results between Python3 and Pypy3.


if __name__ == '__main__':

    n = int(input().strip())
    t = tuple(map(int, input().rstrip().split()))

    print(hash(t))
