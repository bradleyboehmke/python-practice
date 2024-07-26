#!/bin/python3
# https://www.hackerrank.com/challenges/finding-the-percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

scores_of_interest = student_marks[query_name]
avg = round(sum(scores_of_interest)/len(scores_of_interest), 2)
print(f"{avg:.2f}")
