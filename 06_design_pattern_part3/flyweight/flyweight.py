class Stamp:
    def __init__(self, char: str) -> None:
        self.__char = char

    def print_char(self) -> None:
        print(self.__char)


class StampFactory:
    def __init__(self) -> None:
        self.__pool = {}

    def get_stamp(self, char: str) -> Stamp:
        stamp = self.__pool.get(char)

        if stamp:
            return stamp

        new_stamp = Stamp(char)
        self.__pool[char] = new_stamp
        return new_stamp

    def get_pool(self) -> dict[str, Stamp]:
        return self.__pool


if __name__ == "__main__":
    factory = StampFactory()
    stamp1 = factory.get_stamp("A")
    stamp2 = factory.get_stamp("B")
    stamp3 = factory.get_stamp("C")

    stamp1.print_char()
    stamp2.print_char()
    stamp3.print_char()
