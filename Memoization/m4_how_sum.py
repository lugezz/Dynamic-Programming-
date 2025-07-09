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


def how_sum(target: int, numbers: list, memo: dict = {}) -> list:
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        my_remainder = target - number
        this_result = how_sum(my_remainder, numbers, memo)
        if this_result is not None:
            memo[target] = this_result + [number]
            return memo[target]

    memo[target] = None
    return None


print(how_sum(7, [2, 3], {}))  # [2, 2, 3]
print(how_sum(7, [5, 3, 4, 7], {}))  # [3, 4] or [7]
print(how_sum(7, [2, 4], {}))  # None
print(how_sum(8, [2, 3, 5], {}))  # [2, 3, 3] or [5, 3] or [2, 2, 2, 2]
print(how_sum(300, [7, 14], {}))  # Maaany solutions to check but solution in None
