#!/bin/python3
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    max_value = max(list_arr)
    remaining_values = [value for value in list_arr if value != max_value]
    second_max_value = max(remaining_values)
    print(second_max_value)
