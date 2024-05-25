import math


class IEmployee:
    def __init__(self, name: str, mag: float) -> None:
        self.__name = name
        self.__base = 100
        self.__mag = mag

    @property
    def name(self) -> str:
        return self.__name

    def get_bonus(self) -> int:
        return math.floor(self.__base * self.__mag)


class Junior(IEmployee):
    def __init__(self, name: str) -> None:
        MAG = 1.1
        super().__init__(name, MAG)


class Middle(IEmployee):
    def __init__(self, name: str) -> None:
        MAG = 1.5
        super().__init__(name, MAG)


class Senior(IEmployee):
    def __init__(self, name: str) -> None:
        MAG = 2
        super().__init__(name, MAG)


class Expert(IEmployee):
    def __init__(self, name: str) -> None:
        MAG = 3
        super().__init__(name, MAG)


class Professional(IEmployee):
    def __init__(self, name: str) -> None:
        MAG = 5
        super().__init__(name, MAG)


if __name__ == "__main__":
    junior = Junior("Alice")
    middle = Middle("Bob")
    senior = Senior("Carol")
    expert = Expert("David")
    professional = Professional("Eve")

    print(f"{junior.name} get bonus: {junior.get_bonus()}")
    print(f"{middle.name} get bonus: {middle.get_bonus()}")
    print(f"{senior.name} get bonus: {senior.get_bonus()}")
    print(f"{expert.name} get bonus: {expert.get_bonus()}")
    print(f"{professional.name} get bonus: {professional.get_bonus()}")
