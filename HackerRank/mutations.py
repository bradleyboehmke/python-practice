#!/bin/python3
# https://www.hackerrank.com/challenges/python-mutations

def mutate_string(string, position, character):
    list_str = list(string)
    list_str[position] = character
    new_str = ''.join(list_str)
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
