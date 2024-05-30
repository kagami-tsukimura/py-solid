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
        if isinstance(entry, Group):
            print(f"{entry.code}: {entry.name}")
        else:
            print(f"    {entry.code}: {entry.name}")

        [child.accept(self) for child in entry.get_children()]


class CountVisitor(Visitor):
    def __init__(self) -> None:
        self.__group_count = 0
        self.__employee_count = 0

    @property
    def group_count(self) -> int:
        return self.__group_count

    @property
    def employee_count(self) -> int:
        return self.__employee_count

    def visit(self, entry: Entry):
        if isinstance(entry, Group):
            self.__group_count += 1
        else:
            self.__employee_count += 1

        [child.accept(self) for child in entry.get_children()]


if __name__ == "__main__":
    group = Group("001", "group1")
    group.add(Group("002", "group2"))
    group.add(Employee("003", "employee1"))
    group.add(Employee("004", "employee2"))

    visitor = ListVisitor()
    group.accept(visitor)

    count_visitor = CountVisitor()
    group.accept(count_visitor)
