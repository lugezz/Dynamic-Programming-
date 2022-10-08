"""
Write a function that returns the n-th number of the fibonacci sequence.
To generate the next number of the sequence, we sum the previous two. For example,
these are the first 10 fibonacci numbers:
    n	0	1	2	3	4	5	6	7	8	9	10
fib(n)	0	1	1	2	3	5	8	13	21	34	55
"""


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [0] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


def fib(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(n):
        table[i+1] += table[i]
        if i < n-1:
            table[i+2] += table[i]

    return table[n]


print(fib(10))  # 55
print(fib(35))  # 9227465
print(fib(100))  # 354224848179261915075
print(fib(1000))  # a looot
print(fib(2000))  # a huuuge number
