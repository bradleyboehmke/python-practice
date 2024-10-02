# What is the smallest positive integer n such that the factorial of
# n contains at least 100 trailing zeros.  For example, 10 factorial
# does not work because (10x9x8x7x6x5x4x3x2x1) equals 3,628,800 which
# has 2 trailing zeros.

from math import factorial

def trailing_zeros(n):
    s = str(factorial(n))
    zeros = len(s) - len(s.rstrip('0'))
    return zeros

n = 1

while trailing_zeros(n) < 100:
    n += 1

print(n)
