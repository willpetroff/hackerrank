"""

"""

import math
test_cases = []
ntest = int(input())

for _ in range(ntest):
    test_cases.append(int(input()))

for test in test_cases:
    prime_flg = True
    for i in range(2, int(math.sqrt(test))):
        if test % i == 0:
            prime_flg = False
            break
    if test == 1:
        prime_flg = False
    if prime_flg:
        print('Prime')
    else:
        print('Not prime')