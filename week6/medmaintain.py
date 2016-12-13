###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 6
# Median maintenance algorithm using heap data structure
# Created by Zhifei Yan
###############################################

import heapq

# heap_low supports max extraction, heap_high supports min extraction
# Note that heap_low stores negation of original numbers
# Initialize two heaps to contain one integer each
data = open('medmaintain.txt')
int1 = int(next(data).strip())
int2 = int(next(data).strip())
heap_low = []
heap_high = []
if int2 >= int1:
    heapq.heappush(heap_low, -int1)
    heapq.heappush(heap_high, int2)
    med_sum = 2 * int1
else:
    heapq.heappush(heap_low, -int2)
    heapq.heappush(heap_high, int1)
    med_sum = int1 + int2

for int_num in data:
    int_num = int(int_num.strip())
    # Push newly received integer
    if int_num <= heap_high[0]:
        heapq.heappush(heap_low, -int_num)
    else:
        heapq.heappush(heap_high, int_num)
    # After pushing one more integer, check length of two heaps to guarantee that length of heap_low = heap_high or length of heap_low = heap_high + 1
    n_low = len(heap_low)
    n_high = len(heap_high)
    if n_low < n_high:
        heapq.heappush(heap_low, -heapq.heappop(heap_high))
    elif n_low > n_high + 1:
        heapq.heappush(heap_high, -heapq.heappop(heap_low))
    # Accumulate current median, always the max in heap_low
    med_sum = med_sum - heap_low[0]
