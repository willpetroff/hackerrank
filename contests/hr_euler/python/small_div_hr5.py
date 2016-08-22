test_cases = []
tc_num = int(input())
for i in range(tc_num):
    test_cases.append(int(input()))

for test in test_cases:
    found = False
    num = test
    while not found:
        works = []
        for i in range(1, test+1):
            if num % i == 0:
                works.append(i)
        if len(works) == test:
            found = True
        else:
            num += test
    print(num)