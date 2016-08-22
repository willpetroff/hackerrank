test_cases = []
tc_num = int(input())
for i in range(tc_num):
    test_cases.append(int(input()))
for test in test_cases:
    first_num = 1
    last_num = 2
    even_sum = 0
    temp_sum = 0
    while last_num <= test:
        temp_sum = first_num
        first_num = last_num
        if last_num % 2 == 0:
            even_sum += last_num
        last_num = first_num + temp_sum
    print(even_sum)
