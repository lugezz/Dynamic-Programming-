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


def allConstruct(target: str, wordBank: list, memo: dict = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWay = allConstruct(suffix, wordBank, memo)
            totalWay = [[word] + way for way in suffixWay]
            result += totalWay

    memo[target] = result
    return result


print(allConstruct('dog', ['do', 'f', 'g'], {}))  # [['do', 'g']]
print(allConstruct('dog', ['d', 'o', 'g', 'og'], {}))  # [['d', 'o', 'g'], ['d', 'og']]
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef'], {}))  # 3
print(allConstruct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))  # []
print(allConstruct('', ['cat', 'dog', 'mouse'], {}))  # [[]]
print(allConstruct('cat', ['cat', 'dog', 'mouse'], {}))  # [['cat']]
print(allConstruct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse'], {}))  # []
print(allConstruct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse'], {}))  # 4 ways
