from tools import timed_step

"""
Write a function allConstruct(target, wordBank) that accepts a target string and an array of strings.

The function should return a 2D array containing all of the ways that the target can be constructed
by concatenating elements of the wordbank array.

You may reuse elements of 'wordbank' as many times as needed.

allConstruct("", ["any"]) -> [[]]
allConstruct("hello", ["any", "cat"]) -> []
allConstruct("abcde", ["ab", "c", "cde"]) -> [["ab", "cde"]]
allConstruct("purple", ["purp", "purpl", "le", "p", "ur"]) -> [["purp", "le"],["p", "ur", "p", "le"]]
"""


def all_construct(target: str, wordBank: list):
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWay = all_construct(suffix, wordBank)
            totalWay = [[word] + way for way in suffixWay]
            result.extend(totalWay)

    return result


def m_all_construct(target: str, wordBank: list, memo: dict = None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWay = m_all_construct(suffix, wordBank, memo)
            totalWay = [[word] + way for way in suffixWay]
            result.extend(totalWay)

    memo[target] = result
    return result


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g', 'og']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef']),
    ("purple", ["purp", "purpl", "le", "p", "ur"]),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('cat', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'a', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
]

for target, wordBank in test_cases:
    print(f"-------------ALL CONSTRUCT {target} {wordBank} -------------")
    timed_step(f"All Construct ({target}, {wordBank})", all_construct, target, wordBank)
    timed_step(f"All Construct ({target}, {wordBank}) Memoized", m_all_construct, target, wordBank)
    print("-" * 100)
