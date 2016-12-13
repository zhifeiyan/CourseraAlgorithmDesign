# General version of quick sort algorithm via divide and conquer
# Author: Zhifei Yan
# Date: 7/25/16

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    quicksortRecu(arr, 0, len(arr) - 1)

def quicksortRecu(arr, start, end):
    """
    Recursive function
    Always choose middle element as pivot, in-place modify arr list
    """
    # base case
    if start >= end:
        return
    pivot_id = start + (end - start) // 2
    pivot = arr[pivot_id]
    arr[start], arr[pivot_id] = arr[pivot_id], arr[start]
    i = j = start + 1
    while j <= end:
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    # two recursive calls
    quicksortRecu(arr, start, i - 2)
    quicksortRecu(arr, i, end)

