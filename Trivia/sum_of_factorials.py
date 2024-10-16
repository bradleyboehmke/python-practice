# What is the smallest number that is at least 2 digits long where the
# factorials of its digits is equal to the number itself?  For example,
# take the number 40,585.  The sum of the factorials of each digit is:
#   - factorial(4) = 24
#   - factorial(0) = 1
#   - factorial(5) = 120
#   - factorial(8) = 40,320
#   - factorial(5) = 120
# So, 24+1+120+40320+120 = 40,585.  However, is this the smallest digit
# where this is true???

import math

# Function to calculate the sum of factorials of the digits of a number
def sum_of_factorials_of_digits(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

# Loop through numbers to find the smallest factorion
n = 10
while True:
    if sum_of_factorials_of_digits(n) == n:
        break
    n += 1

print(n)
