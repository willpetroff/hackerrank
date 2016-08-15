"""
Given a string, swap each letter's case.
"""
given_str = input()
given_str = list(given_str)
for i in range(len(given_str)):
    if given_str[i].isalpha():
        if ord(given_str[i]) > 96:
            given_str[i] = chr(ord(given_str[i]) - 32)
        else:
            given_str[i] = chr(ord(given_str[i]) + 32)
print("".join(given_str))
