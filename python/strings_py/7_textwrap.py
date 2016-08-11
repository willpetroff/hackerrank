"""
https://www.hackerrank.com/challenges/text-wrap?h_r=next-challenge&h_v=zen
textwrap.wrap(string, max_len)
textwrap.fill(string, max_len)
"""

from textwrap import fill

given_str = input()
max_len = int(input())
print(fill(given_str, max_len))