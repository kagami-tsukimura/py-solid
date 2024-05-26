from abc import ABCMeta, abstractmethod


class Patient:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class IIterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Patient:
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self) -> IIterator:
        pass


class WaitingRoom(Aggregate):
    def __init__(self):
        self.__patients = []

    def get_patients(self) -> list[Patient]:
        return self.__patients
