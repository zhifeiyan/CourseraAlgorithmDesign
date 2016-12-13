###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 2
# Quick sort algorithm exercise 3
# Created by Zhifei Yan
###############################################

def quicksort_ex3(arr, l, r):
    """
    arr: a list of numbers
    l: left-most element index
    r: right-most element index
    Sort the arr in-place using quick sort algorithm
    Return the number of comparisons
    This function chooses pivot using median-of-three
    """
    if l >= r:
        return 0

    # choose pivot
    if r - l > 1:
        first = arr[l]
        last = arr[r]
        if (r - l + 1) % 2 == 0:
            mid_id = l - 1 + (r - l + 1) // 2
            mid = arr[mid_id]
        else:
            mid_id = l + (r - l) // 2
            mid = arr[mid_id]
        three_dict = {first: l, mid: mid_id, last: r}
        pivot = sorted(three_dict)[1]
        pivot_id = three_dict[pivot]
    else:
        pivot = arr[l]
        pivot_id = l

    arr[l], arr[pivot_id] = arr[pivot_id], arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    k1 = quicksort_ex3(arr, l, i - 2)
    k2 = quicksort_ex3(arr, i, r)
    return r - l + k1 + k2

if __name__ == '__main__':
    f = open('input_numbers.txt')
    numbers_list = []
    for line in f:
        numbers_list.append(int(line.strip()))
    num_comp = quicksort_ex3(numbers_list, 0, len(numbers_list) - 1)
