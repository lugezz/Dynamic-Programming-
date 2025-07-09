from tools import timed_step

"""
Write a function countConstruct(target, wordBank) that accepts a target string and an array of strings.
T
he function should return the number of ways that the target can be constructed
by concatenating elements of the wordbank array.

You may reuse elements of 'wordbank' as many times as needed.

Examples:
* countConstruct("", ["any"]) -> 0
* countConstruct("abcde", ["ab", "c", "cde"]) -> 1
* countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef']) -> 2
"""


def count_construct(target: str, wordBank: list):
    total_count = 0
    if target == '':
        return 1

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways = count_construct(suffix, wordBank)
            total_count += num_ways

    return total_count


def m_count_construct(target: str, wordBank: list, memo: dict = None):
    if memo is None:
        memo = {}

    total_count = 0
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways = m_count_construct(suffix, wordBank, memo)
            total_count += num_ways

    memo[target] = total_count
    return total_count


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g', 'og']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef']),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('cat', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe',
     ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee',
      'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
     ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee',
      'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee']),
]

for target, wordBank in test_cases:
    print(f"-------------COUNT CONSTRUCT {target} {wordBank} -------------")
    if len(target) < 30:
        timed_step(f"Count Construct ({target}, {wordBank})", count_construct, target, wordBank)
    timed_step(f"Count Construct ({target}, {wordBank}) Memoized", m_count_construct, target, wordBank)
    print("-" * 100)
