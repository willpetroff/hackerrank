"""
Given a string of numbers (0s and 1s), and two move types (1 space or two spaces), what is the minimum number of moves
to traverse the string without landing on any 1s.
"""

length = int(input())
clouds = [int(num) for num in input().split()]
moves = 0
clouds.pop(0)
while clouds:
    if ((len(clouds) > 1) and clouds[1] == 0) or len(clouds) == 2:
        # print('2 jump')
        clouds = clouds[2:]
    else:
        # print('1 jump')
        clouds = clouds[1:]
    moves += 1
    # print(clouds)
print(moves)
