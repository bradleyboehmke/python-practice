#!/bin/python3
# https://www.hackerrank.com/challenges/python-lists

if __name__ == '__main__':
    N = int(input())
    inputs = {}
    for item in range(N):
        inputs[item] = list(input().rstrip().split())

    my_list = []

    for _, operation in inputs.items():
        if operation[0] == 'insert':
            my_list.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == 'print':
            print(my_list)
        elif operation[0] == 'remove':
            my_list.remove(int(operation[1]))
        elif operation[0] == 'append':
            my_list.append(int(operation[1]))
        elif operation[0] == 'sort':
            my_list.sort()
        elif operation[0] == 'pop':
            my_list.pop()
        elif operation[0] == 'reverse':
            my_list.reverse()
