import sys


from tools import timed_step


sys.setrecursionlimit(2000)


# A naive recursive solution
def fib(n):
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# A memoized solution
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result


print("-------------FIBONACCI 5 -------------")
timed_step("Basic Fibonacci", fib, 5)
timed_step("Memoized Fibonacci", fib_memo, 5)

print("-" * 100)
print("-------------FIBONACCI 35 -------------")
timed_step("Basic Fibonacci", fib, 35)
timed_step("Memoized Fibonacci", fib_memo, 35)

print("-" * 100)
print("-------------FIBONACCI 100 -------------")
# timed_step("Basic Fibonacci", fib, 100)
timed_step("Memoized Fibonacci", fib_memo, 100)

print("-" * 100)
print("-------------FIBONACCI 1000 -------------")
# timed_step("Basic Fibonacci", fib, 1000)
timed_step("Memoized Fibonacci", fib_memo, 1000)
