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


def can_construct(target: str, wordBank: list, memo: dict = {}):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(can_construct('dog', ['do', 'f', 'g'], {}))  # True
print(can_construct('dog', ['d', 'o', 'g'], {}))  # True
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))  # True
print(can_construct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))  # False
print(can_construct('', ['cat', 'dog', 'mouse'], {}))  # True?
print(can_construct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse'], {}))  # False
print(can_construct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'ala', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse'], {}))  # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe',
                    ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee',
                     'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee'], {}))  # True
