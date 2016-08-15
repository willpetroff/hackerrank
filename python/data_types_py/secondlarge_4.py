"""
Given integer N and a series of N numbers, return the second largest.
"""

nums = int(input())
num_arr = [int(i) for i in input().split()]
num_set = {i for i in num_arr}
num_arr = list(num_set)
num_arr.sort()
print(num_arr[-2])
