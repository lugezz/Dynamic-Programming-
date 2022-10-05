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


def canSum(target: int, list_of_nums: list) -> bool:
    resp = False
    minor_values = list(filter(lambda x: x <= target, list_of_nums))

    if len(minor_values) < 1:
        return False

    for value in minor_values:
        if value == target:
            resp = True
            break
        elif value < target:
            resp = canSum(target - value, minor_values)
            if resp:
                break

    return resp


print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))

list_test = [1, 23, 3, 4, 6, 4, 9, 4, 4]
filtered = filter(lambda score: score < 5, list_test)

print(list(filtered))
