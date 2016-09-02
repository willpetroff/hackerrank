"""

"""

arr_len, rot, quer = input().split()
arr = [_ for _ in input().split()]
test_cases = []
for _ in range(int(quer)):
    test_cases.append(input())
for _ in range(int(rot) % len(arr)):
    arr.insert(0, arr.pop())
for index in test_cases:
    print(arr[int(index)])