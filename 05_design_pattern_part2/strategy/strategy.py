from abc import ABCMeta, abstractmethod


class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid in CreditCard for {amount}.")


class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid in Cash for {amount}.")


class ShoppingCart:
    def __init__(self) -> None:
        self.__total = 0
        self.__items = []

    def add_item(self, item: str, price: int) -> None:
        self.__total += price
        self.__items.append((item, price))

    def pay(self, payment_strategy: PaymentStrategy) -> None:
        payment_strategy.pay(self.__total)
