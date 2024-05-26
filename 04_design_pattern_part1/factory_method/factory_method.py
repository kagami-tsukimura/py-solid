from abc import ABCMeta, abstractmethod


class CreditCard(metaclass=ABCMeta):
    def __init__(self, owner: str) -> None:
        self.__owner = owner

    @property
    def owner(self) -> str:
        return self.__owner

    @abstractmethod
    def get_card_type(self) -> str:
        pass

    @abstractmethod
    def get_annual_charge(self) -> int:
        pass
