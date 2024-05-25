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
        return self.__width * self.__height


if __name__ == "__main__":
    r = Rectangle(width=10, height=20)
    print(r.get_area())

    square = Rectangle(width=10, height=10)
    print(square.get_area())
