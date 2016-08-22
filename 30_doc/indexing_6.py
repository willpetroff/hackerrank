num = int(input())
test_cases = []
for _ in range(num):
    test_cases.append(input())

for test in test_cases:
    print(test[0::2], test[1::2])