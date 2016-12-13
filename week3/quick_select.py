# General version of quick select algorithm via divide and conquer
# Author: Zhifei Yan
# Date: 07/25/16

import random

def quickselect(nums, k):
    if not nums:
        return None
    if k < 1 or k > len(nums):
        return None
    return quickselectRecu(nums, 0, len(nums) - 1, k)

def quickselectRecu(nums, start, end, k):
    """
    Note that nums list is modified in-place during each recursive call
    Return the value of kth order statistic
    """
    # base case
    if start == end:
        return nums[start]
    pivot_id = random.randint(start, end)
    pivot = nums[pivot_id]
    nums[start], nums[pivot_id] = nums[pivot_id], nums[start]
    i = start + 1
    # i points to the position of first element > pivot
    for j in range(start + 1, end + 1):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    # relative position of pivot in current searched subarray is i - 1
    nums[start], nums[i - 1] = nums[i - 1], nums[start]
    if i - start == k:
        return pivot
    elif i - start < k:
        return quickselectRecu(nums, i, end, k - i + start)
    else:
        return quickselectRecu(nums, start, i - 2, k)
