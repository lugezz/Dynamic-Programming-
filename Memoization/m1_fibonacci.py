from tools import timed_step


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
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result


# A bottom-up solution
def fib_bottom_up(n):
    if n <= 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


print("-------------FIBONACCI 5 -------------")
timed_step("Basic Fibonacci", fib, 5)
timed_step("Memoized Fibonacci", fib_memo, 5)
timed_step("Bottom-up Fibonacci", fib_bottom_up, 5)

print("-" * 100)
print("-------------FIBONACCI 35 -------------")
timed_step("Basic Fibonacci", fib, 35)
timed_step("Memoized Fibonacci", fib_memo, 35)
timed_step("Bottom-up Fibonacci", fib_bottom_up, 35)

print("-" * 100)
print("-------------FIBONACCI 100 -------------")
# timed_step("Basic Fibonacci", fib, 100)
timed_step("Memoized Fibonacci", fib_memo, 100)
timed_step("Bottom-up Fibonacci", fib_bottom_up, 100)

print("-" * 100)
print("-------------FIBONACCI 1000 -------------")
# timed_step("Basic Fibonacci", fib, 1000)
timed_step("Memoized Fibonacci", fib_memo, 1000)
timed_step("Bottom-up Fibonacci", fib_bottom_up, 1000)
