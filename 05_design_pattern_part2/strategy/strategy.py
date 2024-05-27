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


if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.add_item("Shirt", 100)
    shopping_cart.add_item("Pants", 200)
    credit_payment_strategy = CreditCardPaymentStrategy()
    shopping_cart.pay(credit_payment_strategy)
    shopping_cart.add_item("Shirt", 1000)
    shopping_cart.add_item("Pants", 2000)
    cash_payment_strategy = CashPaymentStrategy()
    shopping_cart.pay(cash_payment_strategy)
