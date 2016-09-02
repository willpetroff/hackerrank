"""
Given an array of n integers and integer k, print the number of (index_1, index_2) pairs where index_1 < index_2
and arr[index_1] + arr[index_2] is evenly divisible by k.
"""

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]

index_pairs = []

for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
        if (arr[i] + arr[j]) % k == 0:
            if (i, j) in index_pairs:
                pass
            else:
                index_pairs.append((i, j))

print(len(index_pairs))
