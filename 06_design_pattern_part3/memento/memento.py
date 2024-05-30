from abc import ABCMeta, abstractmethod


class Memento(metaclass=ABCMeta):
    @abstractmethod
    def get_memo(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, memo: str, date: str) -> None:
        self.__memo = memo
        self.__date = date

    def get_memo(self) -> str:
        return self.__memo
