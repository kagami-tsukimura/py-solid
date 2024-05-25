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
    junior = Junior("Yamada")

    print(f"{junior.name} get bonus: {junior.get_bonus(100)}")
