
# Ways to move in a grid front the top left cell (n, n) to the botton right cell (1, 1)
def grid_traveler(num1: int, num2: int, memo={}):
    key = f'{num1}-{num2}'
    key2 = f'{num2}-{num1}'
    if key in memo:
        return memo[key]
    if key2 in memo:
        return memo[key2]
    if num1 == 1 and num2 == 1:
        return 1

    if num1 == 0 or num2 == 0:
        return 0

    resp = grid_traveler(num1 - 1, num2, memo) + grid_traveler(num1, num2 - 1, memo)
    memo[key] = resp
    memo[key2] = resp
    return resp
    # To consider: grid_traveler(a, b) = grid_traveler(b, a)


print(grid_traveler(1, 1))  # // 1
print(grid_traveler(2, 3))  # // 3
print(grid_traveler(3, 2))  # // 3
print(grid_traveler(3, 3))  # // 6
print(grid_traveler(18, 18))  # // 2333606220
