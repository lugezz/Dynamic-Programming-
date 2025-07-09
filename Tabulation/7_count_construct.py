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


def count_construct(target: str, wordBank: list) -> bool:
    table_len = len(target) + 1
    table = [0] * table_len
    table[0] = 1

    for i in range(table_len):
        if table[i] > 0:
            for word in wordBank:
                if word == target[i:i+len(word)] and i+len(word) < table_len:
                    table[i+len(word)] += table[i]

    return table[table_len-1]


print(count_construct('dog', ['do', 'f', 'g']))  # 1
print(count_construct('dog', ['d', 'o', 'g', 'og']))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'ef']))  # 3
print(count_construct('skatboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct('', ['cat', 'dog', 'mouse']))  # 1
print(count_construct('cat', ['cat', 'dog', 'mouse']))  # 1
print(count_construct('skeleton', ['s', 'k', 'e', 'la', 'loe', 'il', 'on', 'ton', 'dog', 'mouse']))  # 0
print(count_construct('skeleton', ['s', 'k', 'e', 'ton', 'e', 'la', 'le', 'to', 'o', 'n', 'dog', 'mouse']))  # 4
