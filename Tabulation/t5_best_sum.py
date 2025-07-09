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
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target and (table[i+num] is None or len(table[i+num]) > len(table[i]) + 1):
                    table[i + num] = table[i] + [num]

    return table[target]


print(best_sum(7, [2, 3]))  # [2, 2, 3]
print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(7, [2, 4]))  # None
print(best_sum(8, [2, 3, 5]))  # [5, 3]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 3, 25]))  # [25, 25, 25, 25]
print(best_sum(300, [7, 14]))  # Maaany solutions to check but solution in None
