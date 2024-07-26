#!/bin/python3

def compareTriplets(a, b):
    a_points = 0
    b_points = 0

    for a, b in zip(a, b):
        if a > b:
            a_points += 1
        elif b > a:
            b_points += 1

    return [a_points, b_points]

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
