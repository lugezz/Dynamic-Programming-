from tools import timed_step
from memoization.m6_can_construct import can_construct

"""
Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the target can be constructed by
concatenating elements of the wordBank array.

You may reuse elements of wordBank as many times as needed.

Example:

canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) -> True. it can be constructed using 'abc' and 'def'
canConstruct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) -> False. it can't be constructed
canConstruct('', ['cat', 'dog', 'mouse']) -> False. it can't be constructed
"""


def t_can_construct(target: str, wordBank: list) -> bool:
    table_len = len(target) + 1
    table = [False] * table_len
    table[0] = True

    for i in range(table_len):
        if table[i]:
            for word in wordBank:
                if word == target[i:i+len(word)] and i+len(word) < table_len:
                    table[i+len(word)] = True

    return table[table_len-1]


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'ala', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe',
     ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee', 'eeeeeeeee', 'eee',
      'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee'])
]

for target, wordBank in test_cases:
    print(f"-------------CAN CONSTRUCT {target} -------------")
    if len(target) < 30:
        timed_step(f"Can Construct ({target}, {wordBank})", can_construct, target, wordBank)
    timed_step(f"Can Construct ({target}, {wordBank}) Tabulation", t_can_construct, target, wordBank)
    print("-" * 100)
