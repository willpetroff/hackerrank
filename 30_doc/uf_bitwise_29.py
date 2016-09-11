"""

"""

test_cases = []
ntest = int(input())
for _ in range(ntest):
    test_cases.append([int(i) for i in input().split()])

for test in test_cases:
    largest = 0
    start = 1
    while start < test[0]:
        for i in range(start + 1, test[0] + 1):
            bit_and = start & i
            if  test[1] > bit_and > largest:
                largest = bit_and
        start += 1
    print(largest)
