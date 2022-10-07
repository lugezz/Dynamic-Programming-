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


def canConstruct(target: str, wordBank: list, memo: dict = {}):
    if target == '':
        return True

    if target in memo:
        return memo[target]

    for word in wordBank:
        if target.startswith(word):
            resp = canConstruct(target[len(word):], wordBank, memo)
            memo[target] = resp

            if resp:
                return True

    return False

# TODO: Fix

# print(canConstruct('dog', ['do', 'f', 'g']))  # True
# print(canConstruct('dog', ['d', 'o', 'g']))  # True
# print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
# print(canConstruct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
# print(canConstruct('', ['cat', 'dog', 'mouse']))  # False
print(canConstruct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']))  # False
print(canConstruct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'ala', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']))  # True
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe',
                   ['e', 'ee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeee', 'eeeeeeeee', 'eee', 'eeee', 'eeeeee', 'eeeee', 'eeeee', 'eee']))  # True
