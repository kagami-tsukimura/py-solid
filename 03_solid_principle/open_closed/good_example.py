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
    def __init__(self, name: str, mag: float) -> None:
        super().__init__(name, mag)


class Middle(IEmployee):
    def __init__(self, name: str, mag: float) -> None:
        super().__init__(name, mag)


class Senior(IEmployee):
    def __init__(self, name: str, mag: float) -> None:
        super().__init__(name, mag)


class Expert(IEmployee):
    def __init__(self, name: str, mag: float) -> None:
        super().__init__(name, mag)


class Professional(IEmployee):
    def __init__(self, name: str, mag: float) -> None:
        super().__init__(name, mag)


if __name__ == "__main__":
    junior = Junior("Alice", 1.1)
    middle = Middle("Bob", 1.5)
    senior = Senior("Carol", 2)
    expert = Expert("David", 3)
    professional = Professional("Eve", 5)

    print(f"{junior.name} get bonus: {junior.get_bonus()}")
    print(f"{middle.name} get bonus: {middle.get_bonus()}")
    print(f"{senior.name} get bonus: {senior.get_bonus()}")
    print(f"{expert.name} get bonus: {expert.get_bonus()}")
    print(f"{professional.name} get bonus: {professional.get_bonus()}")
