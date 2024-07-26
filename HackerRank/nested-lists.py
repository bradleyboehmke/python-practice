#!/bin/python3
# https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = [record[1] for record in records]
    min_score = min(scores)
    updated_scores = [score for score in scores if score != min_score]
    second_low_score = sorted(updated_scores)[0]

    second_low_names = []

    for name, score in records:
        if score == second_low_score:
            second_low_names.append(name)

    second_low_names = sorted(second_low_names)
    for name in second_low_names:
        print(name)
