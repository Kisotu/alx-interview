#!/usr/bin/python3
"""The prime game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game with 'xx turns
    """
    if x < 1 or not nums:
        return None
    wins_by_maria, wins_by_ben = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes < n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        wins_by_ben += primes_count % 2 == 0
        wins_by_maria += primes_count % 2 == 1
    if wins_by_maria == wins_by_ben:
        return None
    return 'Maria' if wins_by_maria > wins_by_ben else 'Ben'
