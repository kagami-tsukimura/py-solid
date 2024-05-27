from abc import ABCMeta, abstractmethod


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def draw(self) -> None:
        pass


class Button(metaclass=ABCMeta):
    @abstractmethod
    def draw(self) -> None:
        pass
