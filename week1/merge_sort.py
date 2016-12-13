# General version of merge sort algorithm via divide and conquer
# Author: Zhifei Yan
# Date: 7/25/16

def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    return mergesortRecu(arr, 0, n - 1)

def mergesortRecu(arr, start, end):
    """
    Recursive function
    Return sorted copy of arr list, do not in-place modify it
    """
    # base case
    if start == end:
        return [arr[start]]
    mid = start + (end - start) // 2
    # list of sorted copy of first half
    arr1 = mergesortRecu(arr, start, mid)
    # list of sorted copy of of second half
    arr2 = mergesortRecu(arr, mid + 1, end)
    # merge
    sorted_arr = []
    i = j = 0
    len1, len2 = mid - start + 1, end - mid
    while i < len1 and j < len2:
        if arr1[i] <= arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    if i == len1:
        sorted_arr.extend(arr2[j:])
    else:
        sorted_arr.extend(arr1[i:])
    return sorted_arr
