from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self):
        self.__width = 0
        self.__height = 0

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    def get_area(self) -> int:
        return self.width * self.height


class Square(Shape):
    def __init__(self):
        self.__length = 0

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    def get_area(self) -> int:
        return self.length**2


if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.width = 10
    rectangle.height = 30
    print(rectangle.get_area())

    square = Square()
    square.length = 15
    print(square.get_area())
