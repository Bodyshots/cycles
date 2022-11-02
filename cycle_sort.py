from typing import List
"""
According to Wikipedia, cycle sort is meant to minimize the number of writes required to sort
an array. So, in light of its terrible worst-case, best-case, and average-case performance
(O(n^2)), this module is confirm the advantages cycle sort has over other in-place sorting
algorithms.

"""

def cycle_sort(arr: List[int]) -> int:
    """
    Return the elements of <arr> in ascending order using cycle permutations.
    Also, print the:
        - Cycle permutations created while sorting
        - The total number of writes performed 
    
    >>> test1 = []
    >>> cycle_sort(test1)
    0
    >>> print(test1)
    []
    >>> test2 = [5, 3, 2, 1, 4]
    >>> cycle_sort(test2)
    3
    >>> print(test2)
    [1, 2, 3, 4, 5]
    >>> test3 = [9, 120, 2, 14, 13, 0]
    >>> cycle_sort(test3)
    4
    >>> print(test3)
    [0, 2, 9, 13, 14, 120]

    """
    writes = 0
    arr_len = len(arr)
    i = 0
    while arr != [] and i != arr_len - 1: # arr[arr_len - 1] already sorted by definition
        nums_less_than = i
        # Explanation: Anything before the index i must be less than
        # arr[i], as these indices are in their "correct" positions
        for j in range(i + 1, arr_len): # i + 1 to ignore considering the curr elem
            if arr[i] > arr[j]: 
                nums_less_than += 1
        
        if (i != nums_less_than):
            arr[i], arr[nums_less_than] = arr[nums_less_than], arr[i]
            writes += 1

        else: i += 1 # one cycle

    return writes



def bubble_sort(arr: List[int]) -> List[int]:
    """
    Return the elements of <arr> in ascending order using bubble sort.
    Also, print the total number of writes performed
    
    Bubble sort is typically known as the "worst" sorting in-place
    sorting algorithm (O(n^2) for everything).
    >>> test1 = []
    >>> bubble_sort(test1)
    0
    >>> print(test1)
    []
    >>> test2 = [5, 3, 2, 1, 4]
    >>> bubble_sort(test2)
    7
    >>> print(test2)
    [1, 2, 3, 4, 5]
    >>> test3 = [9, 120, 2, 14, 13, 0]
    >>> bubble_sort(test3)
    12
    >>> print(test3)
    [0, 2, 9, 13, 14, 120]
    """
    writes = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                writes += 1

    return writes

def quick_sort(arr: List[int]) -> List[int]:
    """
    Return the elements of <arr> in ascending order using quick sort.
    Also, print the total number of writes performed
    
    Quick sort is typically regarded as one of the best in-place
    sorting algorithms, especially in its average case running time (O(nlogn))

    >>> test1 = []
    >>> quick_sort(test1)
    0
    >>> print(test1)
    []
    >>> test2 = [5, 3, 2, 1, 4]
    >>> quick_sort(test2)
    17
    >>> print(test2)
    [1, 2, 3, 4, 5]
    >>> test3 = [9, 120, 2, 14, 13, 0]
    >>> quick_sort(test3)
    20
    >>> print(test3)
    [0, 2, 9, 13, 14, 120]
    """
    writes = 0
    return partition(arr, 0, len(arr) - 1)

def partition(arr: List[int], first, last) -> int:
    if last - first + 1 == 0: 
        return 0
    if last - first + 1 == 1:
        if arr[last] < arr[first]: 
            arr[first], arr[last] = arr[last], arr[first]
        return 1
    i = first - 1 # indicates #s smaller than pivot
    j = first # iterates through array
    writes = 0
    pivot = arr[last]
    while (j != last):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            writes += 1
        j += 1
    
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    writes += 1

    writes += partition(arr, first, i)
    writes += partition(arr, i + 1, last)
    return writes


if __name__ == "__main__":
    import doctest
    doctest.testmod()