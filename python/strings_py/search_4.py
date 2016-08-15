"""
Given a string and a string fragment, print the index value of the string fragment
"""

given_string = input()
given_fragment = input()
end_index = len(given_fragment)
counter = 0
for i in range(len(given_string)-(end_index-1)):
    if given_string[i:i+end_index] == given_fragment:
        counter += 1
print(counter)
