from __future__ import annotations

from abc import ABCMeta, abstractmethod
from copy import deepcopy


class ItemPrototype(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__review: list[str] = []

    def __str__(self) -> str:
        return f"{self.__name}: {self.__review}"

    @abstractmethod
    def clone(self) -> ItemPrototype:
        """原型を複製する"""
        pass
