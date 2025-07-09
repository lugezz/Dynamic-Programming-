from tools import timed_step
from memoization.m5_best_sum import best_sum

"""
Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of
numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.

Example:
howSum(7, [5, 3, 4, 7]) -> Could be 3 + 4 or 7. But [7] is the shorter result
"""


def t_best_sum(target: int, numbers: list) -> list:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target and (table[i+num] is None or len(table[i+num]) > len(table[i]) + 1):
                    table[i + num] = table[i] + [num]

    return table[target]


test_cases = [
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
    (100, [1, 2, 5, 3, 25]),
    (300, [7, 14]),
]

for target, numbers in test_cases:
    print(f"-------------BEST SUM {target} -------------")
    if target < 100 and len(numbers) < 10:
        timed_step(f"Best Sum ({target}, {numbers})", best_sum, target, numbers)
    timed_step(f"Best Sum ({target}, {numbers}) Tabulation", t_best_sum, target, numbers)
    print("-" * 100)
