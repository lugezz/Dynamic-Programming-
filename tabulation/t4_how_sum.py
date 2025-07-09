from tools import timed_step
from memoization.m4_how_sum import how_sum

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


def t_how_sum(target: int, numbers: list) -> list:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = table[i] + [num]

    return table[target]


test_cases = [
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
    (157, [14, 16, 20]),
    (300, [7, 14]),
    (300, [2, 14]),
]

for target, numbers in test_cases:
    print(f"-------------HOW SUM {target} -------------")
    if target < 200 and len(numbers) < 10:
        timed_step(f"How Sum ({target}, {numbers})", how_sum, target, numbers)
    timed_step(f"How Sum ({target}, {numbers}) Tabulation", t_how_sum, target, numbers)
    print("-" * 100)
