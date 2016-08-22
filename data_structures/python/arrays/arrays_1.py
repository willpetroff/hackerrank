"""
Print array items in reverse order.
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(1, n + 1):
    print(arr[i * -1], end=' ')

# Can also do:
# arr.sort(reverse=True)
# print(" ".join([str(item) for item in arr]))