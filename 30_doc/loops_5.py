"""
Given int N, multiply N by every number 1-10.
"""

num = int(input())
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, i * num))
