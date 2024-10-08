prime = []

for num in range(1, 1001):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime.append(num)

max_prime = max(prime)
sum_of_parts = sum(int(digit) for digit in str(max_prime))

print(max_prime, sum_of_parts)
