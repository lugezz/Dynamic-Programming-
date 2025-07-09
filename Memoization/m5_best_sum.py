from tools import timed_step

"""
Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of
numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.

Example:
howSum(7, [5, 3, 4, 7]) -> Could be 3 + 4 or 7. But [7] is the shorter result
"""


def best_sum(target: int, numbers: list) -> list:
    if target == 0:
        return []

    if target < 0:
        return None

    shorter_combination = None
    for number in numbers:
        my_remainder = target - number
        this_result = best_sum(my_remainder, numbers)

        if this_result is not None:
            combination = this_result + [number]

            if not shorter_combination or len(combination) < len(shorter_combination):
                shorter_combination = combination

    return shorter_combination


def m_best_sum(target: int, numbers: list, memo: dict = None) -> list:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return []

    if target < 0:
        return None

    shorter_combination = None
    for number in numbers:
        my_remainder = target - number
        this_result = m_best_sum(my_remainder, numbers, memo)

        if this_result is not None:
            combination = this_result + [number]

            if not shorter_combination or len(combination) < len(shorter_combination):
                shorter_combination = combination

    memo[target] = shorter_combination

    return shorter_combination


tests_cases = [
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
    (8, [1, 4, 5]),
    (20, [1, 2, 5, 3, 10]),
    (100, [1, 2, 5, 3, 25]),
    (300, [7, 14]),
]


for target, numbers in tests_cases:
    print(f"-------------BEST SUM {target} {numbers} -------------")
    if target < 30:
        timed_step(f"Best Sum ({target}, {numbers})", best_sum, target, numbers)
    timed_step(f"Best Sum ({target}, {numbers}) Memoized", m_best_sum, target, numbers)
    print("-" * 100)
