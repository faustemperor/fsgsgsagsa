class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self._height = new_height

    def area(self):
        return self._width * self._height

rect = Rectangle(10, 5)
rect.width = 15
print(rect.area())