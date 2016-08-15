"""
Given a number of commands to be given, and commands on each line, write a function that modifies lists.
"""


def func_exec(list_arr, command, *args):
    if command == 'insert':
        list_arr.insert(int(args[0]), int(args[1]))
    elif command == 'remove':
        list_arr.remove(int(args[0]))
    elif command == 'append':
        list_arr.append(int(args[0]))
    elif command == 'sort':
        list_arr.sort()
    elif command == 'pop':
        list_arr.pop()
    elif command == 'reverse':
        list_arr.reverse()
    elif command == 'print':
        print(list_arr)
    elif command == 'count':
        list_arr.count(args[0])
    elif command == 'index':
        list_arr.index(args[0])
    else:
        print('Unknown Command. Please Try Again.')


arr = []
runs = int(input())
for _ in range(runs):
    func_exec(arr, *input().split())
