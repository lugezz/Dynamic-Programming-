from tools import timed_step


# Ways to move in a grid front the top left cell (n, n) to the botton right cell (1, 1)
def grid_traveler(num1: int, num2: int, memo={}):
    """
    Calculate the number of ways to travel in a grid from the top left cell (num1
    , num2) to the bottom right cell (1, 1).
    The function uses memoization to store previously computed results for
    efficiency.
    """

    key = f'{num1}-{num2}'
    key2 = f'{num2}-{num1}'
    # grid_traveler(a, b) = grid_traveler(b, a)
    if key in memo:
        return memo[key]
    if key2 in memo:
        return memo[key2]

    if num1 < 0 or num2 < 0:
        raise ValueError("num1 and num2 must be non-negative integers")

    if num1 == 0 or num2 == 0:
        return 0

    if num1 == 1 or num2 == 1:
        return 1

    resp = grid_traveler(num1 - 1, num2, memo) + grid_traveler(num1, num2 - 1, memo)
    memo[key] = resp
    memo[key2] = resp
    return resp


timed_step("Grid Traveler (1, 1)", grid_traveler, 1, 1)  # // 1
timed_step("Grid Traveler (2, 3)", grid_traveler, 2, 3)  # // 3
timed_step("Grid Traveler (3, 2)", grid_traveler, 3, 2)  # // 3
timed_step("Grid Traveler (3, 3)", grid_traveler, 3, 3)  # // 6
timed_step("Grid Traveler (18, 18)", grid_traveler, 18, 18)  # // 2333606220
