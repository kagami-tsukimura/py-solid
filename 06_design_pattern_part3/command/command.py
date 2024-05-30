from abc import ABCMeta, abstractmethod


class File:
    def __init__(self, name: str) -> None:
        self.__name = name

    def open(self) -> None:
        print(f"open file: {self.__name}")

    def compress(self) -> None:
        print(f"compress file: {self.__name}")

    def close(self) -> None:
        print(f"close file: {self.__name}")


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass


class OpenCommand(Command):
    def __init__(self, file: File) -> None:
        self.__file = file

    def execute(self) -> None:
        self.__file.open()
