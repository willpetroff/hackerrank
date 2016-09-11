"""

"""

ret_day, ret_month, ret_year = (int(i) for i in input().split())
exp_day, exp_month, exp_year = (int(i) for i in input().split())

if ret_year == exp_year:
    if ret_month == exp_month:
        if ret_day == exp_day:
            print (0)
        elif ret_day <= exp_day:
            print(0)
        else:
            print((ret_day - exp_day) * 15)
    elif ret_month <= exp_month:
        print(0)
    else:
        print((ret_month - exp_month) * 500)
elif ret_year <= exp_year:
    print(0)
else:
    print(10000)