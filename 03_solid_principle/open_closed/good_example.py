import math
from abc import ABCMeta, abstractmethod


class IEmployee(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass


class Junior(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.1)


class Middle(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.5)


class Senior(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 2)


class Expert(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 3)


if __name__ == "__main__":
    base_bonus = 100
    junior = Junior("Alice")
    middle = Middle("Bob")
    senior = Senior("Carol")
    expert = Expert("David")

    print(f"{junior.name} get bonus: {junior.get_bonus(base_bonus)}")
    print(f"{middle.name} get bonus: {middle.get_bonus(base_bonus)}")
    print(f"{senior.name} get bonus: {senior.get_bonus(base_bonus)}")
    print(f"{expert.name} get bonus: {expert.get_bonus(base_bonus)}")
