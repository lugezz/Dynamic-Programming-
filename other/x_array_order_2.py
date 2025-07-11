"""
Python3 program to find minimum number of swaps required to sort an array

Return the minimum number of swaps required to sort the array
"""


def min_swap(arr, n):
    """ Function to find minimum number of swaps required to sort the array.
    The function returns the minimum number of swaps required to sort the array.
    The function uses a hashmap to store the indexes of the input array and sorts the
    array to find the correct positions of the elements. It then swaps the elements to
    their correct positions and updates the indexes in the hashmap accordingly.
    """
    ans = 0
    temp = arr.copy()
    temp.sort()

    # Dictionary which stores the
    # indexes of the input array
    h = {}

    for i in range(n):
        h[arr[i]] = i

    init = 0

    for i in range(n):
        # This is checking whether the current element is at the right place or not
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]

            # If not, swap this element with the index of the element which should come here
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

            # Update the indexes in the hashmap accordingly
            h[init] = h[temp[i]]
            h[temp[i]] = i

    return ans


# Driver code
a = [101, 758, 315, 730, 472, 619, 460, 479]
n = len(a)

# Output will be 5
print(min_swap(a, n))

# This code is contributed by avanitrachhadiya2155
