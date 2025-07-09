from tools import timed_step

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


def can_construct(target: str, wordBank: list) -> bool:
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, wordBank):
                return True

    return False


def m_can_construct(target: str, wordBank: list, memo: dict = None) -> bool:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if m_can_construct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'ala', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe',
     ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee',
      'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
     ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee',
      'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee']),
]


for target, wordBank in test_cases:
    print(f"-------------CAN CONSTRUCT {target} {wordBank} -------------")
    if len(target) < 30:
        timed_step(f"Can Construct ({target}, {wordBank})", can_construct, target, wordBank)
    timed_step(f"Can Construct ({target}, {wordBank}) Memoized", m_can_construct, target, wordBank)
    print("-" * 100)
