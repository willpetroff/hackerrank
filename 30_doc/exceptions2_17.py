"""

"""


# Write your code here
class Calculator:
    def __init__(self):
        pass

    def power(self, num_1, num_2):
        if num_1 < 0 or num_2 < 0:
            power_error = ValueError('n and p should be non-negative')
            raise power_error
        return num_1 ** num_2


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
