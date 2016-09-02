"""

"""

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

changes = True
swaps = 0
last_index_counter = 1
while changes:
    changes = False
    for ind in range(len(a)-last_index_counter):
        if a[ind] > a[ind+1]:
            a[ind], a[ind+1] = a[ind+1], a[ind]
            swaps += 1
            changes = True
    last_index_counter += 1

print('Array is sorted in {} swaps.'.format(swaps))
print('First Element:', a[0])
print('Last Element:', a[-1])