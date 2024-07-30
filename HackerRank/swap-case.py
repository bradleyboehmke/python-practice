#!/bin/python3
# https://www.hackerrank.com/challenges/swap-case


def swap_case(s):
    new_s = ''

    for location, letter in enumerate(s):
        if letter.isupper():
            new_s = new_s + letter.lower()
        elif letter.islower():
            new_s = new_s + letter.upper()
        else:
            new_s = new_s + letter

    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
