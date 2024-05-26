from __future__ import annotations

from abc import ABCMeta, abstractmethod
from copy import copy, deepcopy


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


class DeepCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        # 自分自身をdeep copy
        return deepcopy(self)


class ShallowCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        # 自分自身をshallow copy
        return copy(self)


class ItemManager:
    def __init__(self) -> None:
        self.items = {}

    def register_item(self, key: str, item: ItemPrototype) -> None:
        self.items[key] = item

    def create(self, key: str) -> ItemPrototype:
        if key in self.items:
            item = self.items[key]
            return item.create_copy()
        raise Exception(f"{key} is not found.")


if __name__ == "__main__":
    manager = ItemManager()
    manager.register_item("deep", DeepCopyItem("deep"))
    manager.register_item("shallow", ShallowCopyItem("shallow"))

    deep = manager.create("deep")
    shallow = manager.create("shallow")

    print(deep)
    print(shallow)
