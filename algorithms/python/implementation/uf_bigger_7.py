"""

"""
test_cases = []
num = int(input())
for _ in range(num):
    temp = [char for char in input()]
    test_cases.append(temp)

for case in test_cases:
    swap = False
    for index in range(1, len(case)):
        index *= -1
        if case[index] > case[index-1]:
            case[index], case[index - 1] = case[index - 1], case[index]
            swap = True
            break

    if swap:
        print(''.join(case))
    else:
        print('no answer')
