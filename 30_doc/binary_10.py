"""
Given an integer, convert to binary and print out the length of the largest consecutive sequence of '1's
"""

n = int(input().strip())
n_str = [i for i in bin(n)[2:]]
count = 0
highest = 0
for i in n_str:
    if i == '1':
        count += 1
        if count > highest:
            highest = count
    else:
        count = 0
print(highest)
print(n_str)