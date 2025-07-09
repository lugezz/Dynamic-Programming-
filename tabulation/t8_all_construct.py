from tools import timed_step
from memoization.m8_all_construct import all_construct

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


def t_all_construct(target: str, wordBank: list) -> bool:
    table = [[] for x in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in wordBank:
            if (target[i: i + len(word)] == word):
                newCombination = [prevCombination + [word] for prevCombination in table[i]]
                table[i + len(word)].extend(newCombination)
    return table[-1]


test_cases = [
    ('dog', ['do', 'f', 'g']),
    ('dog', ['d', 'o', 'g', 'og']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'ef']),
    ('purple', ['purp', 'purpl', 'le', 'p', 'ur']),
    ('skatboard', ['skat']),
    ('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('', ['cat', 'dog', 'mouse']),
    ('cat', ['cat', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']),
    ('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']),
]

for target, wordBank in test_cases:
    print(f"-------------ALL CONSTRUCT {target} -------------")
    if len(target) < 30:
        timed_step(f"All Construct ({target}, {wordBank})", all_construct, target, wordBank)
    timed_step(f"All Construct ({target}, {wordBank}) Tabulation", t_all_construct, target, wordBank)
    print("-" * 100)
