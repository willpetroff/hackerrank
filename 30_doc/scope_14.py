"""

"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here

    maximumDifference = 0

    def computeDifference(self):
        maximum = 0
        for num_1 in range(len(self.__elements)-1):
            for num_2 in range(num_1 + 1, len(self.__elements)):
                diff = abs(self.__elements[num_1] - self.__elements[num_2])
                if diff > maximum:
                    maximum = diff
        self.maximumDifference = maximum


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)