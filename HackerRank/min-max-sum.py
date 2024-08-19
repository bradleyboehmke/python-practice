#!/bin/python3
# https://www.hackerrank.com/challenges/mini-max-sum

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    large_sum = sum(sorted(arr)[:4])
    small_sum = sum(sorted(arr, reverse=True)[:4])
    return print(large_sum, small_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
