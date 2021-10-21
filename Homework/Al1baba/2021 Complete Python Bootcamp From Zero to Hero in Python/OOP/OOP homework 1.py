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

    def __init__(self, height, radius):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * pow(self.radius, 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * pow(self.radius, 2)


pringles = Cylinder(2, 3)
print(pringles.volume())
print(pringles.surface_area())


















