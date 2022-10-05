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


def canSum(target: int, numbers: list, memo={}) -> bool:
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        my_remainder = target - number
        if canSum(my_remainder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


print(canSum(7, [2, 3], {}))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4], {}))  # False
print(canSum(8, [2, 3, 5], {}))  # True
print(canSum(300, [7, 14], {}))  # False
