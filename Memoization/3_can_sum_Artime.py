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


def basic_can_sum(target: int, list_of_nums: list) -> bool:
    resp = False
    minor_values = sorted(list(filter(lambda x: x <= target, list_of_nums)))

    if len(minor_values) < 1:
        return False

    for value in minor_values:
        if value == target:
            resp = True
            break
        elif value < target:
            resp = can_sum(target - value, minor_values)
            if resp:
                break

    return resp


def can_sum(target: int, list_of_nums: list, memo={}) -> bool:
    resp = False
    minor_values = sorted(list(filter(lambda x: x <= target, list_of_nums)))

    list_test_str = [str(x) for x in list_of_nums]
    list_to_text = "-".join(list_test_str)
    key = f'{str(target)}|{list_to_text}'

    if len(minor_values) < 1:
        return False

    if key in memo:
        return memo[key]

    for value in minor_values:
        if value == target:
            resp = True
            break
        elif value < target:
            resp = can_sum(target - value, minor_values)
            if resp:
                break

    memo[key] = resp
    return resp


print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(67, [2, 3, 4, 8, 5, 14, 9, 11, 25, 3, 19, 4, 14, 15, 16, 17]))
# False because # list -> False, target -> even
print(can_sum(67, [2, 4, 4, 8, 6, 14, 10, 12, 26, 2, 20, 4, 14, 18, 16, 22]))
