from tools import timed_step
from memoization.m7_count_construct import count_construct

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


def t_count_construct(target: str, wordBank: list) -> bool:
    table_len = len(target) + 1
    table = [0] * table_len
    table[0] = 1

    for i in range(table_len):
        if table[i] > 0:
            for word in wordBank:
                if word == target[i:i+len(word)] and i+len(word) < table_len:
                    table[i+len(word)] += table[i]

    return table[table_len-1]


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g', 'og']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'ef']),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('cat', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
]

for target, wordBank in test_cases:
    print(f"-------------COUNT CONSTRUCT {target} -------------")
    if len(target) < 30:
        timed_step(f"Count Construct ({target}, {wordBank})", count_construct, target, wordBank)
    timed_step(f"Count Construct ({target}, {wordBank}) Tabulation", t_count_construct, target, wordBank)
    print("-" * 100)
