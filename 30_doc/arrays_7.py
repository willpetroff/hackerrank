"""
Given an array, print the array in reverse order.
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for num in arr[::-1]:
    print(num, end=' ')