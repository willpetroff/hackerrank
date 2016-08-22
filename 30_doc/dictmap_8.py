"""

"""

num = int(input())
phoneNum = dict(input().split() for _ in range(num))
while True:
    try:
        test = input()
        print("{}={}".format(test, phoneNum[test]) if test in phoneNum else 'Not found')
    except:
        break
