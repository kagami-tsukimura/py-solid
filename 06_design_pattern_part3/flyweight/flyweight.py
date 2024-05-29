class Stamp:
    def __init__(self, char: str) -> None:
        self.__char = char

    def print_char(self) -> None:
        print(self.__char)


class StampFactory:
    def __init__(self) -> None:
        self.__pool = {}

    def get_stamp(self, char: str) -> Stamp:
        if char not in self.__pool:
            self.__pool[char] = Stamp(char)
        return self.__pool[char]
