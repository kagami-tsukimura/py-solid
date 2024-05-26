from __future__ import annotations

from abc import ABCMeta, abstractmethod
from copy import deepcopy


class ItemPrototype(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__review: list[str] = []

    def __str__(self) -> str:
        return f"{self.__name}: {self.__review}"

    def set_review(self, review: str) -> None:
        self.__review.append(review)

    @abstractmethod
    def create_copy(self) -> ItemPrototype:
        pass
