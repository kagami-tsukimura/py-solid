import datetime
import re
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, expression: str, date: datetime.date):
        self.validate(expression)
        self.__expression = expression
        self.__date = date

    def validate(self, expression: str) -> None:
        if not re.match(r"\d{4}-\d{2}-\d{2}", expression):
            raise ValueError(f"Invalid expression: {expression}")


class AbstractExpression(metaclass=ABCMeta):
    def interpret(self, context: Context) -> None:
        pass
