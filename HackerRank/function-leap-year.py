# https://www.hackerrank.com/challenges/write-a-function

def is_leap(year):
    leap = False

    # The year can be evenly divided by 4, is a leap year
    is_div_by_4 = year % 4 == 0

    # The year can be evenly divided by 100, it is NOT a leap year unless
    # it is also divisible by 400
    is_div_by_100 = year % 100 == 0
    is_div_by_400 = year % 400 == 0

    if is_div_by_4:
        leap = True
        if is_div_by_100 and not is_div_by_400:
            leap = False
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))
