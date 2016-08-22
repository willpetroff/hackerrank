"""

"""


def sieve_erat(limit):
    limit_plus = limit + 1
    list_one = [i for i in range(limit_plus)]
    list_one[1] = 0
    for i in range(2, int(limit ** .5) + 1):
        if list_one[i]:
            list_one[i * i:limit_plus:i] = [0] * len(range(i * i, limit_plus, i))
    return list(filter(None, list_one))

test_cases = []
tc_num = int(input())
for i in range(tc_num):
    test_cases.append(int(input()))

for test in test_cases:
    print(sieve_erat(test**2)[test-1])
