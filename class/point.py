import math


class Point:
    """point obj
        members are x and y"""
    def __init__(self, x, y):
        """create a point obj"""
        self.x = x
        self.y = y

    def distance(self, point):
        x = (point.x - self.x)**2
        y = (point.y - self.y)**2
        return math.sqrt(x + y)


class Rect:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def diagonal(self):
        return self.top_left.distance(self.bottom_right)

    def height(self):
        return math.fabs(self.top_left.x - self.bottom_right.x)

    def length(self):
        return math.fabs(self.top_left.y - self.bottom_right.y)

    def area(self):
        return self.height()* self.length()


class Cube:
    def __init__(self, top_left, bottom_right, width):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.width = width

    def get_height(self):
        return math.fabs(self.top_left.x - self.bottom_right.x)

    def get_length(self):
        return math.fabs(self.top_left.y - self.bottom_right.y)

    def get_width(self):
        return self.width

    def get_volume(self):
        return self.get_height()*self.get_length()*self.get_width()


myRect = Rect(Point(2, 3), Point(5, 5))
print(myRect.area())

myCube = Cube(Point(2, 3), Point(5, 5), 5)
print(myCube.get_volume()) 