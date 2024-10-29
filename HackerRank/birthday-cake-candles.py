# You are in charge of the cake for a child's birthday. You have decided the
# cake will have one candle for each year of their total age. They will only
# be able to blow out the tallest of the candles. Count how many candles are
# tallest.
# https://www.hackerrank.com/challenges/birthday-cake-candles


def birthdayCakeCandles(candles):
    candles = [int(d) for d in str(candles[0])]
    max_height = max(candles)
    count = candles.count(max_height)
    return count

if __name__ == '__main__':

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
