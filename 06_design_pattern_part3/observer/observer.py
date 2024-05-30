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

    @abstractmethod
    def restock(self) -> None:
        pass


class TvGameSubject(ItemSubject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__in_stock = False

    def restock(self) -> None:
        print("restocked!")
        self.__in_stock = True
        self.notify()


if __name__ == "__main__":
    store = StoreObserver()
    personal = PersonalObserver()
    tv_game = TvGameSubject("RPG Game")

    tv_game.attach(store)
    tv_game.attach(personal)
    tv_game.restock()
