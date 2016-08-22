"""

"""

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]


for num in range(len(a)):
    if a[num] < b[num]:
        a[num] = 0
    elif a[num] == b[num]:
        a[num] = 0
        b[num] = 0
    else:
        b[num] = 0
print(len(list(filter(None,a))), len(list(filter(None,b))))
