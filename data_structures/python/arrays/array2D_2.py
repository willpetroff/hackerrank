"""
Given a 6x6 array, print the largest "hourglass" sum.
"""

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

results = []

for row in range(0, 4):
    for col in range(0, 4):
        hg_sums = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1]\
              + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
        results.append(hg_sums)

results.sort()
print(results[-1])
