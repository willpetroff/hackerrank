"""
Given n:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""

given_int = int(input())
if (given_int % 2 != 0) or (given_int % 2 == 0 and 6 <= given_int <= 20):
    print("Weird")
else:
    print("Not Weird")
