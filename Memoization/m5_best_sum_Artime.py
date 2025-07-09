"""
Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of
numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.

Example:
howSum(7, [5, 3, 4, 7]) -> Could be 3 + 4 or 7. But [7] is the shorter result
"""


def best_sum(target: int, numbers: list, memo: dict = {}) -> list:
    temp_result = None
    if target in memo:
        return memo[target]
    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        my_remainder = target - number
        this_result = best_sum(my_remainder, numbers, memo)

        if this_result is not None:
            this_result = this_result + [number]

            if not temp_result:
                temp_result = this_result
            elif len(this_result) < len(temp_result):
                temp_result = this_result

    memo[target] = temp_result

    return temp_result


print(best_sum(7, [2, 3], {}))  # [2, 2, 3]
print(best_sum(7, [5, 3, 4, 7], {}))  # [7]
print(best_sum(7, [2, 4], {}))  # None
print(best_sum(8, [1, 4, 5], {}))  # [4, 4]
print(best_sum(8, [2, 3, 5], {}))  # [5, 3]
print(best_sum(100, [1, 2, 5, 3, 25], {}))  # [25, 25, 25, 25]
print(best_sum(300, [7, 14], {}))  # Maaany solutions to check but solution in None
