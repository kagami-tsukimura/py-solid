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


class CompressCommand(Command):
    def __init__(self, file: File) -> None:
        self.__file = file

    def execute(self) -> None:
        self.__file.compress()


class CloseCommand(Command):
    def __init__(self, file: File) -> None:
        self.__file = file

    def execute(self) -> None:
        self.__file.close()


class Queue:
    def __init__(self) -> None:
        self.__commands: list[Command] = []

    def add_command(self, command: Command) -> None:
        self.__commands.append(command)

    def execute(self) -> None:
        for command in self.__commands:
            command.execute()


if __name__ == "__main__":
    file = File("test.txt")

    OpenCommand(file).execute()
    CompressCommand(file).execute()
