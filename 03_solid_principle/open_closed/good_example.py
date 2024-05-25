import math
from abc import ABCMeta, abstractmethod


class IEmployee(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass
