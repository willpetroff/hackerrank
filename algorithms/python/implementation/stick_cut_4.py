"""

"""
from time import time
from random import randint


# Method one:
def method_1(arr):
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


# Method two:
def method_2(n, arr):
    container = [0] * 1001
    for i in arr:
        container[i] += 1
    ans = [n]
    counter = n
    for j in container:
        if j > 0:
            counter -= j
            ans.append(counter)
    ans.pop()
    for answer in ans:
        print(answer)

num = int(input().strip())
array = [randint(1, 1000) for _ in range(1000)]  # [int(arr_temp) for arr_temp in input().strip().split(' ')]
start_time = time()
method_1(array)
time_1 = time() - start_time
start_time = time()
method_2(num, array)
time_2 = time() - start_time
print(time_1, time_2)

'''
num = int(input().strip())
array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
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
'''