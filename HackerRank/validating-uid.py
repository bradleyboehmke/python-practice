#!/bin/python3
# https://www.hackerrank.com/challenges/validating-uid
import re
from collections import Counter


if __name__ == '__main__':

    n = int(input().strip())
    uids = []
    for item in range(n):
        uids.append(input().rstrip())

    for uid in uids:
        violations = 0

        # at least 2 uppercase alpha
        upper_case = re.findall('[A-Z]', uid)
        if len(upper_case) < 2:
            violations += 1

        # must contain at least 3 digits
        digits = re.findall('[0-9]', uid)
        if len(digits) < 3:
            violations += 1

        # can only contain a-z, A-Z, & 0-9
        bad_characters = re.findall('[^a-zA-Z0-9]', uid)
        if bad_characters:
            violations += 1

        # no repeating characters
        repetition = Counter(uid).most_common()[0][1] > 1
        if repetition:
            violations += 1

        # must be 10 characters
        wrong_len = len(uid) != 10
        if wrong_len:
            violations += 1

        if violations == 0:
            print("Valid")
        else:
            print("Invalid")
