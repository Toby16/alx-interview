#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    """
    Function: is_prime
    => to check if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Function: isWinner
    => to determine the winner of the game
    """

    winners = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        n = nums[i]
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        turn = 'Maria'

        while len(primes) > 0:
            to_remove = -1
            for j in range(len(primes)):
                if n % primes[j] == 0:
                    to_remove = primes[j]
                    break

            if to_remove != -1:
                primes = [num for num in primes if num % to_remove != 0]
                turn = 'Maria' if turn == 'Ben' else 'Ben'
            else:
                break

        if turn == 'Maria':
            winners['Maria'] += 1
        else:
            winners['Ben'] += 1

    max_wins = max(winners.values())
    result = [key for key, value in winners.items() if value == max_wins]

    if len(result) > 1:
        return None
    else:
        return result[0]


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
