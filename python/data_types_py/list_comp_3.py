"""
Given three numbers, x, y, and z, and a sum return a list of lists containing [x,y,z] where x+y+z != sum.
"""

x = int(input())
y = int(input())
z = int(input())
total = int(input())

print([[x1, y1, z1] for x1 in range(x + 1) for y1 in range(y + 1) for z1 in range(z + 1) if x1 + y1 + z1 != total])
