#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    n = len(arr)
    positive = 0
    negative = 0
    zero = 0

    for item in arr:
        if item > 0:
            positive += 1
        elif item < 0:
            negative += 1
        elif item == 0:
            zero += 1

    pos_ratio = round(positive / n, 6)
    neg_ratio = round(negative / n, 6)
    zer_ratio = round(zero / n, 6)

    print(f'{pos_ratio:.6f}')
    print(f'{neg_ratio:.6f}')
    print(f'{zer_ratio:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
