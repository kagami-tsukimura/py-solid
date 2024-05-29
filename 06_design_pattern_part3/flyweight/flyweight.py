class Stamp:
    def __init__(self, char: str) -> None:
        self.__char = char

    def print_char(self) -> None:
        print(self.__char)


class StampFactory:
    def __init__(self) -> None:
        self.__pool = {}