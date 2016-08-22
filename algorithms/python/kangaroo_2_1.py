"""
Given a two starting spots (x1, x2; where x2>x1) and two move distances (v1,v2), determine if they will land on the
same spot at the same time.
"""

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if v2 >= v1:  # Weeds out instances where second starts after and moves farther than first
    print('NO')
elif (x2 - x1) % (v2 - v1) == 0:
    print('YES')
else:
    print('NO')
