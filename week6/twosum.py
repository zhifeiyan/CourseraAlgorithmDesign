###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 6
# A variant of two-sum algorithm
# Created by Zhifei Yan
###############################################

# read integers as keys of a dictionary (hash table)
data = {}
for line in open('twosum.txt'):
    data[int(line.strip())] = None

count = 0
for t in range(-10 ** 4, 10 ** 4 + 1):
    for x in data:
        if (t - x) in data and (t - x) != x:
            count += 1
            break

out = open('result.txt', 'wt')
print(count, file=out)
out.close()
