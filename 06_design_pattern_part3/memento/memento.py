import datetime
from abc import ABCMeta, abstractmethod


class Memento(metaclass=ABCMeta):
    @abstractmethod
    def get_memo(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, memo: str, date: str) -> None:
        self.__memo = memo
        self.__date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_memo(self) -> str:
        return self.__memo

    def __str__(self) -> str:
        return f"{self.__date}: {self.__memo}"


class Notepad:
    def __init__(self, memo: str) -> None:
        self.__memo = memo

    def get_memo(self) -> str:
        return self.__memo

    def add_memo(self, memo: str) -> None:
        self.__memo = memo

    def save(self) -> Memento:
        print("Memo saved.")
        return ConcreteMemento(self.get_memo())

    def restore(self, memento: Memento) -> None:
        self.add_memo(memento.get_memo())
        print("Memo restored.")


class Caretaker:
    def __init__(self, notepad: Notepad, mementos: list[Memento]) -> None:
        self.__notopad = notepad
        self.__mementos = mementos

    def add_memento(self, memento: Memento) -> None:
        self.__mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self.__mementos[index]
