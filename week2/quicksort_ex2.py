###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 2
# Quick sort algorithm exercise 2
# Created by Zhifei Yan
###############################################

def quicksort_ex2(arr, l, r):
    """
    arr: a list of numbers
    l: left-most element index
    r: right-most element index
    Sort the arr in-place using quick sort algorithm
    Return the number of comparisons
    This function always chooses the last element of array as pivot
    """
    if l >= r:
        return 0

    pivot = arr[r]
    arr[l], arr[r] = arr[r], arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    k1 = quicksort_ex2(arr, l, i - 2)
    k2 = quicksort_ex2(arr, i, r)
    return r - l + k1 + k2

if __name__ == '__main__':
    f = open('input_numbers.txt')
    numbers_list = []
    for line in f:
        numbers_list.append(int(line.strip()))
    num_comp = quicksort_ex2(numbers_list, 0, len(numbers_list) - 1)
