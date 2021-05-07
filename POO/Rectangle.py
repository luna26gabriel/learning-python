class Rectangle:
    
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Square(Rectangle):

    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.lenght*self.width

class Cube(Rectangle):

    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.lenght*self.width*self.height


square = Square(2, 4)
cube = Cube(2, 4, 2)

print(square.area())
print(cube.volume())