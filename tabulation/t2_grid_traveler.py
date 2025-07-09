from tools import timed_step
from memoization.m2_grid_traveler import grid_traveler

"""
Say you are a traveler on a 2D grid.
You begin in the top-left corner
and your goal is to travel to the bottom-right corner.
You may only move down and right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Examples:

grid_traveler(1, 1) => 1
grid_traveler(3, 2) => 3
grid_traveler(3, 3) => 6
"""


def t_grid_traveler(m: int, n: int) -> int:

    matrix = [[0] * (n+1) for i in range(m+1)]
    matrix[1][1] = 1

    for i in range(m+1):
        for j in range(n+1):
            my_val = matrix[i][j]
            if i+1 <= m:
                matrix[i+1][j] += my_val
            if j+1 <= n:
                matrix[i][j+1] += my_val

    return matrix[m][n]


test_cases = [
    (1, 1),
    (2, 3),
    (3, 2),
    (3, 3),
    (9, 14),
    (14, 14),
    (18, 18),
]

for m, n in test_cases:
    print(f"-------------GRID TRAVELER {m}x{n} -------------")
    if m < 15 and n < 15:
        timed_step(f"Grid Traveler ({m}, {n})", grid_traveler, m, n)
    timed_step(f"Grid Traveler ({m}, {n}) Tabulation", t_grid_traveler, m, n)
    print("-" * 100)
