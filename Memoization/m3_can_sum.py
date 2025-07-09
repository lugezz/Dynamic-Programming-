from tools import timed_step

"""
Write a function `canSum(targetSum, numbers)` that takes in a
targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it
is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input members are nonnegative.

Example:
canSum(7, [5, 3, 4, 7]) -> True because 3 + 4 = 7
canSum(7, [2, 4]) -> False
"""


def can_sum(target: int, numbers: list) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        my_remainder = target - number
        if can_sum(my_remainder, numbers):
            return True

    return False


def m_can_sum(target: int, numbers: list, memo=None) -> bool:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        my_remainder = target - number
        if m_can_sum(my_remainder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


test_cases = [
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
    (50, [2, 3, 5]),
    (97, [7, 14]),
    (300, [7, 14]),
]


for target, numbers in test_cases:
    print(f"-------------CAN SUM {target} {numbers} -------------")
    if target < 100:
        timed_step(f"Can Sum ({target}, {numbers})", can_sum, target, numbers)
    timed_step(f"Can Sum ({target}, {numbers}) Memoized", m_can_sum, target, numbers)
    print("-" * 100)
