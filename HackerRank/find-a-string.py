# In this challenge, the user enters a string and a substring. You have to
# print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    first_letter = 0
    last_letter = len(sub_string)
    match_count = 0

    while last_letter <= len(string):
        sub = string[first_letter:last_letter]
        if sub == sub_string:
            match_count += 1

        first_letter += 1
        last_letter += 1

    return match_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
