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
    * Change comes from within
    makeChange: Function to determine
                the fewest number of coins needed
                to meet a given amount (total)

    Args:
        coins - List of coins of different values (list)
        total - given amount (int)
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # The value of a coin will always be an integer greater than 0
    """
    # Gather all coins that are greater than 0
    # and 'less then or equal to `total`'
    """
    if len(coins) != 0:
        new_coins = [i for i in coins if ((i > 0) and (i <= total))]

    """
    Create a list to store the minimum number of coins needed
    for each amount from 0 to the total.
    """
    dp = [float('inf')] * (total + 1)

    # The minimum number of coins needed to make 0 is 0.
    dp[0] = 0

    # Iterate through all coin values.
    for coin in new_coins:
        """
        Update dp[i] if using this coin reduces the number of coins needed
        to make amount i.
        """
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # The result is stored in dp[total].
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
