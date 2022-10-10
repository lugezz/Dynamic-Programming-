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


def howSum(target: int, numbers: list) -> list:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = table[i] + [num]

    return table[target]


print(howSum(7, [2, 3]))  # [2, 2, 3]
print(howSum(7, [5, 3, 4, 7]))  # [3, 4] or [7]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 3, 3] or [5, 3] or [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # Maaany solutions to check but solution in None
