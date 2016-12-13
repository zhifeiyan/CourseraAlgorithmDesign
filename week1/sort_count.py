###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 1
# Merge sort algorithm
# Created by Zhifei Yan
###############################################

def sort_count(arr, n):
    """
    arr: a list of integers
    n: length of arr
    """
    if n == 1:
        return arr, 0
    arr1 = arr[:n // 2]
    arr2 = arr[n // 2:]
    arr1_sort, count1 = sort_count(arr1, n // 2)
    arr2_sort, count2 = sort_count(arr2, n - n // 2)

    # Merge and count split inversion
    i = 0
    j = 0
    count3 = 0
    arr_sort = []
    for k in range(n):
        if arr1_sort[i] <= arr2_sort[j]:
            arr_sort.append(arr1_sort[i])
            if i < n // 2 - 1:
                i += 1
            else:
                arr_remain = arr2_sort[j:]
                break
        else:
            arr_sort.append(arr2_sort[j])
            count3 = count3 + n // 2 - i
            if j < n - n // 2 - 1:
                j += 1
            else:
                arr_remain = arr1_sort[i:]
                break
    arr_sort.extend(arr_remain)
    return arr_sort, count1 + count2 + count3

if __name__ == '__main__':
    number_list = []
    for line in open('numbers.txt'):
        number_list.append(int(line.strip()))
    _, count = sort_count(number_list, len(number_list))
