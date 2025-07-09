from tools import timed_step
from memoization.m3_can_sum import can_sum

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


def t_can_sum(target: int, numbers: list) -> bool:
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target+1):
        if table[i]:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = True

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
    print(f"-------------CAN SUM {target} -------------")
    if target < 200 and len(numbers) < 10:
        timed_step(f"Can Sum ({target}, {numbers})", can_sum, target, numbers)
    timed_step(f"Can Sum ({target}, {numbers}) Tabulation", t_can_sum, target, numbers)
    print("-" * 100)
