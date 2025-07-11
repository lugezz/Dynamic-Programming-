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


def can_construct(target, wordBank):
    if target == '':
        return False

    for word in wordBank:
        if len(word) > len(target):
            continue
        if word == target:
            return True
        if word == target[:len(word)]:
            resp = can_construct(target[len(word):], wordBank)
            if resp:
                return True

    return False


print(can_construct('dog', ['do', 'f', 'g']))  # True
print(can_construct('dog', ['d', 'o', 'g']))  # True
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print(can_construct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'board']))  # True
print(can_construct('', ['cat', 'dog', 'mouse']))  # False
print(can_construct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']))  # False
print(can_construct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'ala', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']))  # True
