"""
Given a series of user-supplied numbers, create a tuple.
"""

arr_length = int(input())
a_tup = tuple(int(i) for i in input().split())
print(hash(a_tup))
