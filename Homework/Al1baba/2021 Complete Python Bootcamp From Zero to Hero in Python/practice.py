import math

# Problem 1 make a  class that can calculate distance and slope of any 2d coordinate

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        d = math.sqrt(pow(self.coor2[0] - self.coor1[0], 2) + pow(self.coor2[1] - self.coor1[1], 2))
        return d

    def slope(self):
        s = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return s


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())



# Problem 2 Make a cylinder class that can calculate its volume and surface area


class Cylinder:

    def __init__(self, height, width):
        self.width = width
        self.height = height




















