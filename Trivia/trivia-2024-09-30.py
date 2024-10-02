# What is the smallest positive two digit integer n such that the sum of
# the squares of the digits of n is equal to 100. For example, the number
# 26 does not work because 2^2 + 6^2 != 100.
def sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

n = 1
while True:
    if sum_of_squares_of_digits(n) == 100:
        break
    n += 1

print(n)
