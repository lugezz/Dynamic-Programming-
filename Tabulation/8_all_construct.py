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


def all_construct(target: str, wordBank: list) -> bool:
    table = [[] for x in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in wordBank:
            if (target[i: i + len(word)] == word):
                newCombination = [prevCombination + [word] for prevCombination in table[i]]
                table[i + len(word)].extend(newCombination)
    return table[-1]


print(all_construct('dog', ['do', 'f', 'g']))  # [['do', 'g']]
print(all_construct('dog', ['d', 'o', 'g', 'og']))  # [['d', 'o', 'g'], ['d', 'og']]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef']))  # 3
print(all_construct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # []
print(all_construct('', ['cat', 'dog', 'mouse']))  # [[]]
print(all_construct('cat', ['cat', 'dog', 'mouse']))  # [['cat']]
print(all_construct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']))  # []
print(all_construct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']))  # 4 ways
