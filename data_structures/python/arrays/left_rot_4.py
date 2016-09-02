"""

"""

num, rot = (int(num) for num in input().split())
arr = [char for char in input().split()]
if rot < num:
    arr = arr[rot:] + arr[:rot]
else:
    arr = arr[-(num % rot):] + arr[:-(num % rot)]
for i in arr:
    print(i, end=" ")
