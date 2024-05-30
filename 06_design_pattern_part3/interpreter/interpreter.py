import datetime
import re
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, expression: str, date: datetime.date):
        self.validate(expression)
        self.__expression = expression
        self.__date = date

    def validate(self, expression: str) -> None:
        if len(expression) != 10 or not bool(
            re.match("(?=.*YYYY)(?=.*MM)(?=.*DD)", expression)
        ):
            raise ValueError(f"Invalid expression: {expression}")


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context: Context) -> None:
        pass


class YearExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> None:
        if context.expression[0:4] == "YYYY":
            self.__child = context.expression[4:]
        else:
            raise ValueError(f"Invalid expression: {context.expression}")

    def __str__(self) -> str:
        return f"YearExpression: {self.__child}"
