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


class Platinum(CreditCard):
    def get_card_type(self) -> str:
        return "Platinum"

    def get_annual_charge(self) -> int:
        return 50000


class Gold(CreditCard):
    def get_card_type(self) -> str:
        return "Gold"

    def get_annual_charge(self) -> int:
        return 10000


class CreditCardFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_credit_card(self, owner: str) -> CreditCard:
        pass

    @abstractmethod
    def register_credit_card(self, card: CreditCard) -> None:
        pass


class CreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        pass

    def register_credit_card(self, card: CreditCard) -> None:
        pass

    def create(self, owner: str) -> CreditCard:
        credit_card = self.create_credit_card(owner)
        self.register_credit_card(credit_card)
        return credit_card


credit_card_database: list[CreditCard] = []
