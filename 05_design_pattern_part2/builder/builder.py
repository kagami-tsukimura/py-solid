from abc import ABCMeta, abstractmethod


class Computer:
    def __init__(self):
        self.type = None
        self.cpu = None
        self.ram = None

    def __str__(self):
        return f"{self.type} {self.cpu} {self.ram}"


class ComputerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_cpu(self, cpu: str) -> None:
        pass

    @abstractmethod
    def add_ram(self, ram: int) -> None:
        pass


class DesktopBuilder(ComputerBuilder):
    def __init__(self):
        self.__computer = Computer()
        self.__computer.type = "Desktop"

    def add_cpu(self, cpu: str) -> None:
        self.__computer.cpu = cpu

    def add_ram(self, ram: int) -> None:
        self.__computer.ram = ram

    def get_result(self) -> Computer:
        return self.__computer
