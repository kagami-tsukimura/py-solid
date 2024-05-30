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
    def interpret(self, context: Context) -> None:
        pass
