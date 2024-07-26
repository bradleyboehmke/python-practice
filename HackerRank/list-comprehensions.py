#!/bin/python3
# https://www.hackerrank.com/challenges/list-comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_options = range(x + 1)
    y_options = range(y + 1)
    z_options = range(z + 1)

    possible_options = [[x, y, z] for x in x_options
                                  for y in y_options
                                  for z in z_options]

    meets_criteria = [sum(l) != n for l in possible_options]
    combos = list(zip(possible_options, meets_criteria))
    result = [option for option, criteria in combos if criteria]
    print(result)
