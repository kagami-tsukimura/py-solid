from abc import ABCMeta, abstractmethod


class Memento(metaclass=ABCMeta):
    @abstractmethod
    def get_memo(self) -> str:
        pass
