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
