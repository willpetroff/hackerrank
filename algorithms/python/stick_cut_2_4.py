"""

"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
while arr:
    print(len(arr))
    min_len = arr[0]
    count = 0
    for ind in range(len(arr)):
        arr[ind] -= min_len
        if arr[ind] == 0:
            count += 1
    arr = arr[count:]