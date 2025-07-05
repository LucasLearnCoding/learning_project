class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_height(self, value):
        self.height = value

    def set_width(self, value):
        self.width = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        rectangle = ("*" * self.width + "\n") * self.height
        return rectangle
    def get_amount_inside(self, shape):
        return (self.height*self.width) // (shape.height * shape.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, value):
        self.set_height(value)
        self.set_width(value)

    def set_width(self, value):
        super().set_width(value)
        self.height = value

    def set_height(self, value):
        super().set_height(value)
        self.width = value

# Example usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect)  # Rectangle(width =10, height = 5)
    print("Area:", rect.get_area())  # Area: 50
    print("Perimeter:", rect.get_perimeter())  # Perimeter: 30
    print("Diagonal:", rect.get_diagonal())  # Diagonal: 11.180339887498949
    print("Picture:\n", rect.get_picture())  # Picture of rectangle

    square = Square(7)
    print(square)  # Square(side = 7)
    square.set_side(5)
    print(square)  # Square(side = 5)
    print("Area of square:", square.get_area())  # Area of square: 25
    print("Picture of square:\n", square.get_picture())  # Picture of square
    print(Rectangle(15,10).get_amount_inside(Square(5)))

