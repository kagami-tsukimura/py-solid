from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    def __init__(self, code: str, name: str) -> None:
        self.__code = code
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_children(self) -> list[Entry]:
        pass

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Group(Entry):
    def __init__(self, code: str, name: str) -> None:
        super().__init__(code, name)
        self.__entries: list[Entry] = []

    def add(self, entry: Entry) -> None:
        self.__entries.append(entry)

    def get_children(self) -> list[Entry]:
        return self.__entries

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_group(self)
