#classes

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return 'Rectangle: width = {0}, height = {1}'.format(self._width, self._height)

    def get_width(self):
        return self._width

    def set_width(self):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    def get_height(self):
        return self._height

    def set_height(self):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height



    def __repr__(self): #representation dunders methods
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle): # check to see if other is a Rectangle
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,20)

print(r1.width)
print(r1.area())
print(r1.perimeter())

r2 = Rectangle(10,10)

print(r1 is not r2)

print(r1 == r2)

print(r1 == 100)

print(r2 < r1)
