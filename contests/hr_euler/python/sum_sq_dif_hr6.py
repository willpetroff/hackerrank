"""

"""


def sum_squares(num):
    return (num * (num + 1) * (2 * num + 1)) / 6

def square_sum(num):
    return sum([i for i in range(1, num+1)])**2

test_cases = []
tc_num = int(input())
for i in range(tc_num):
    test_cases.append(int(input()))

for test in test_cases:
    print(int(square_sum(test)-sum_squares(test)))
