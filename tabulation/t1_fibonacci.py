from tools import timed_step
from memoization.m1_fibonacci import fib

"""
Write a function that returns the n-th number of the fibonacci sequence.
To generate the next number of the sequence, we sum the previous two. For example,
these are the first 10 fibonacci numbers:
    n	0	1	2	3	4	5	6	7	8	9	10
fib(n)	0	1	1	2	3	5	8	13	21	34	55
"""


def t_fib(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(n):
        table[i+1] += table[i]
        if i < n-1:
            table[i+2] += table[i]

    return table[n]


test_cases = [10, 35, 50, 100, 1000]

for n in test_cases:
    print(f"-------------FIBONACCI {n} -------------")
    if n < 50:
        timed_step(f"Fibonacci ({n})", fib, n)
    timed_step(f"Fibonacci ({n}) Tabulation", t_fib, n)
    print("-" * 100)
