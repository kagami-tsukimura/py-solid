from abc import ABCMeta, abstractmethod


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self) -> None:
        pass


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self) -> None:
        pass
