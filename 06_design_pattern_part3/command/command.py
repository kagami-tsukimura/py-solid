from abc import ABCMeta, abstractmethod


class File:
    def __init__(self, name: str) -> None:
        self.__name = name

    def open(self) -> None:
        print(f"open file: {self.__name}")


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass
