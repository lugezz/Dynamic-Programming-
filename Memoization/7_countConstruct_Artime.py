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


def countConstruct(target: str, wordBank: list, memo: dict = {}):
    result = 0
    if target in memo:
        return memo[target]

    if target == '':
        return 0

    for word in wordBank:
        if word == target:
            result += 1

        elif target.startswith(word):
            suffix = target[len(word):]
            result += countConstruct(suffix, wordBank, memo)

    memo[target] = result
    return result


print(countConstruct('dog', ['do', 'f', 'g'], {}))  # 1
print(countConstruct('dog', ['d', 'o', 'g', 'og'], {}))  # 2
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef'], {}))  # 3
print(countConstruct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))  # 0
print(countConstruct('', ['cat', 'dog', 'mouse'], {}))  # 0
print(countConstruct('cat', ['cat', 'dog', 'mouse'], {}))  # 1
print(countConstruct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse'], {}))  # 0
print(countConstruct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse'], {}))  # 4
