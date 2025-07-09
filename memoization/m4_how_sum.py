from tools import timed_step


"""
Write a function howSum(targetSum, numbers) that takes in a target sum and an array
of numbers as arguments.

The function should return an array containing any combination of elements that add
up to exactly the target sum. If there is no combination that adds up to the target sum,
then return null.

If there are multiple combinations possible, you may return any single one.

Example:
howSum(7, [5, 3, 4, 7]) -> Could be 3 + 4 or 7
howSum(7, [2, 4]) -> Returns None
howSum(0, [3, 4]) -> Returns []
"""


def how_sum(target: int, numbers: list) -> list:
    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        my_remainder = target - number
        this_result = how_sum(my_remainder, numbers)
        if this_result is not None:
            return this_result + [number]
    return None


def m_how_sum(target: int, numbers: list, memo: dict = None) -> list:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        my_remainder = target - number
        this_result = m_how_sum(my_remainder, numbers, memo)
        if this_result is not None:
            memo[target] = this_result + [number]
            return memo[target]

    memo[target] = None
    return None


test_cases = [
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
    (197, [16, 5, 14]),
    (300, [7, 14]),
]


for target, numbers in test_cases:
    print(f"-------------HOW SUM {target} {numbers} -------------")
    if target < 200:
        timed_step(f"How Sum ({target}, {numbers})", how_sum, target, numbers)
    timed_step(f"How Sum ({target}, {numbers}) Memoized", m_how_sum, target, numbers)
    print("-" * 100)
