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
    def set_type(self) -> None:
        pass

    @abstractmethod
    def set_cpu(self) -> None:
        pass

    @abstractmethod
    def set_ram(self) -> None:
        pass
