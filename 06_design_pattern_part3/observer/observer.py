from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, name: str) -> None:
        pass


class StoreObserver(Observer):
    def update(self, name: str) -> None:
        print(f"{name} is updated")
