"""
Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of
numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.

Example:
howSum(7, [5, 3, 4, 7]) -> Could be 3 + 4 or 7. But [7] is the shorter result
"""


def bestSum(target: int, numbers: list, memo: dict = {}) -> list:
    temp_result = ''
    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        my_remainder = target - number
        this_result = bestSum(my_remainder, numbers, memo)

        if this_result is not None:
            temp_result = this_result + [number]
            if target in memo and memo[target]:
                print(number, numbers, temp_result, memo[target])
                if len(temp_result) < len(memo[target]):
                    memo[target] = temp_result
            else:
                memo[target] = temp_result

    memo[target] = None
    return None

# TODO: Fix


print(bestSum(7, [2, 3], {}))  # [2, 2, 3]
print(bestSum(7, [5, 3, 4, 7], {}))  # [7]
print(bestSum(7, [2, 4], {}))  # None
print(bestSum(8, [2, 3, 5], {}))  # [5, 3]
print(bestSum(300, [7, 14], {}))  # Maaany solutions to check but solution in None
