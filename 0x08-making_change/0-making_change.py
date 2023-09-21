#!/usr/bin/python3
"""
Making Change
ALX Interview
Change comes from within

Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount (total)
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make a given amount (total).

    Args:
        coins - List of coin values (list of ints)
        total - Target amount (int)

    Returns:
        The minimum number of coins needed to make the total.
        If it's not possible to make the total with the given coins, return -1.
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # The value of a coin will always be an integer greater than 0
    """
    # Gather all coins that are greater than 0
    # and 'less then or equal to `total`'
    """
    if len(coins) != 0:
        new_coins = [i for i in coins if ((i > 0) and (i <= total))]

    # Initialize a list
    # to store the minimum number of coins for each amount from 0 to total.
    dp = [float('inf')] * (total + 1)

    # The minimum number of coins needed to make 0 is 0.
    dp[0] = 0

    # Iterate through each coin value.
    for coin in new_coins:
        # Update dp[i] if using this coin reduces the number of coins needed
        # to make amount i.
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'),
    # it means it's not possible to make the total with given coins.
    if dp[total] == float('inf'):
        return -1

    return dp[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
