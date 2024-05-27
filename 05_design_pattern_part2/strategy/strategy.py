from abc import ABCMeta, abstractmethod


class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid in cash for {amount}.")
