# If you're on a Number Theory kick, here is one of my favorites: A
# an integer n is a perfect power if it can be expressed as m^k with
# m and k integers and k > 1. For example, 25 is a perfect power because
# 25 = 5^2. Find two consecutive integers that are perfect powers. How
# many can you find?

def find_perfect_powers(limit):
    perfect_powers = set()
    # Iterate over potential base values
    for x in range(2, int(limit ** 0.5) + 1):
        y = 2
        power = x ** y
        # Keep increasing the exponent as long as the power is within the limit
        while power <= limit:
            perfect_powers.add(power)
            y += 1
            power = x ** y
    return sorted(perfect_powers)

# Example: Find all perfect powers up to 1,000,000,000
limit = 1000000000
perfect_powers = find_perfect_powers(limit)

perfect_pairs = []
for i in range(len(perfect_powers)):
    j = i+1
    if j > len(perfect_powers)-1:
        break

    item1 = perfect_powers[i]
    item2 = perfect_powers[j]
    if item2 - item1 == 1:
        perfect_pairs.append((item1, item2))

print(perfect_pairs)
