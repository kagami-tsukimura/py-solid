import math


class IEmployee:
    def __init__(self, name: str, base: int, mag: float) -> None:
        self.__name = name
        self.__base = base
        self.__mag = mag

    @property
    def name(self) -> str:
        return self.__name

    def get_bonus(self) -> int:
        return math.floor(self.__base * self.__mag)


class Junior(IEmployee):
    def __init__(self, name: str, base: int, mag: float) -> None:
        super().__init__(name, base, mag)


class Middle(IEmployee):
    def __init__(self, name: str, base: int, mag: float) -> None:
        super().__init__(name, base, mag)


class Senior(IEmployee):
    def __init__(self, name: str, base: int, mag: float) -> None:
        super().__init__(name, base, mag)


class Expert(IEmployee):
    def __init__(self, name: str, base: int, mag: float) -> None:
        super().__init__(name, base, mag)


class Professional(IEmployee):
    def __init__(self, name: str, base: int, mag: float) -> None:
        super().__init__(name, base, mag)


if __name__ == "__main__":
    base_bonus = 100
    junior = Junior("Alice", base_bonus, 1.1)
    middle = Middle("Bob", base_bonus, 1.1)
    senior = Senior("Carol", base_bonus, 1.1)
    expert = Expert("David", base_bonus, 1.1)
    professional = Professional("Eve", base_bonus, 1.1)

    print(f"base bonus: {base_bonus}")
    print(f"{junior.name} get bonus: {junior.get_bonus()}")
    print(f"{middle.name} get bonus: {middle.get_bonus()}")
    print(f"{senior.name} get bonus: {senior.get_bonus()}")
    print(f"{expert.name} get bonus: {expert.get_bonus()}")
    print(f"{professional.name} get bonus: {professional.get_bonus()}")
