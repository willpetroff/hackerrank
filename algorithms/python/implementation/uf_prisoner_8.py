"""

"""

test_cases = []
num = int(input())
for _ in range(num):
    test_cases.append(input().split())

for test in test_cases:
    prisoners = int(test[0])
    sweets = int(test[1])
    start = int(test[2])
    if (sweets + start) <= prisoners:
        print(sweets + start - 1)
    else:
        print(sweets % (prisoners - start + 1))
