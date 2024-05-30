from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, name: str) -> None:
        pass


class StoreObserver(Observer):
    def update(self, name: str) -> None:
        print(f"{name} is Arrival. Let's purchase it!")


class PersonalObserver(Observer):
    def update(self, name: str) -> None:
        print(f"{name} is Arrival. Let's buy it!")


class ItemSubject(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self.__name)
