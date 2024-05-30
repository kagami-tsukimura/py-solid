from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, name: str):
        pass


class StoreObserver(Observer):
    def update(self, name: str):
        print(f"{name} is updated")
