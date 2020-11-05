#classes

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width = {0}, height = {1}'.format(self.width, self.height)

    def __repr__(self): #representation dunders methods
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

r1 = Rectangle(10,20)

print(r1.width)
print(r1.area())
print(r1.perimeter())

r2 = Rectangle(10,20)

print(r1 is not r2)

print(r1 == r2)
