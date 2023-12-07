#!/usr/bin/python3
"""Prime game module
"""


def is_prime(n):
    """ True if n is prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def delete_num(n, nums):
    """ Remove multiples of n
    """
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x, nums):
    """ Return name of the player who won most rounds
    """
    nums.sort()
    Maria, Ben = 0, 0

    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0

        while any(is_prime(n) for n in nums2 if n > 1):
            for i, n in enumerate(nums2):
                if n > 1 and is_prime(n):
                    delete_num(n, nums2)
                    turn += 1
                    break

        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1

    if Maria == Ben:
        return None
    return "Maria" if Maria > Ben else "Ben"
