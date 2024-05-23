from practice2 import Rectangle, Square


def main() -> None:
    rect = Rectangle(width=10, height=20)
    print(rect.calc_area())

    square = Square(length=7)
    print(square.calc_area())


if __name__ == "__main__":
    main()
