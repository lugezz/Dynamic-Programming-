
"""
Given an array of size n such that array elements are in range from
1 to n. The task is to count a number of move-to-front
operations to arrange items as {1, 2, 3,… n}. The move-to-front operation
is to pick any item and place it in first position.

This problem can also be seen as a stack of items with only move available
is to pull an item from the stack and placing it on top of the stack.

Examples :

Input: arr[] = {3, 2, 1, 4}.
Output: 2
First, we pull out 2 and places it on top,
so the array becomes (2, 3, 1, 4). After that,
pull out 1 and becomes (1, 2, 3, 4).

Input:  arr[] = {5, 7, 4, 3, 2, 6, 1}
Output:  6
We pull elements in following order
7, 6, 5, 4, 3 and 2

Input: arr[] = {4, 3, 2, 1}.
Output: 3
"""

list1 = [3, 2, 1, 4]
list2 = [5, 7, 4, 3, 2, 6, 1]
list3 = [4, 3, 2, 1]


def minMoves(arr, n):

    # Since we traverse array from end,
    # expected item is initially n
    expectedItem = n

    # Traverse array from end
    for i in range(n - 1, -1, -1):

        # If current item is at its
        # correct position, decrement
        # the expectedItem (which also
        # means decrement in minimum
        # number of moves)
        if (arr[i] == expectedItem):
            expectedItem -= 1
    return expectedItem


print("List1 Result:", minMoves(list1, 4))
print("List2 Result:", minMoves(list2, 7))
print("List3 Result:", minMoves(list3, 4))
