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
        visitor.visit(self)


class Employee(Entry):
    def __init__(self, code: str, name: str) -> None:
        super().__init__(code, name)

    def get_children(self) -> list[Entry]:
        return []

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, entry: Entry) -> None:
        pass


class ListVisitor(Visitor):
    def visit(self, entry: Entry):
        if type(entry) == Group:
            print("f{entry.code}: {entry.name}")
