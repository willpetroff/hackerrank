"""
Change a character at a given index to a given character.
"""

given_str = input()
given_index, given_char = input().split()
given_str = list(given_str)
given_str[int(given_index)] = given_char
print("".join(given_str))