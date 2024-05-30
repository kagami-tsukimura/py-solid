import datetime
import re
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, expression: str, date: datetime.date):
        self.validate(expression)
        self.__expression = expression
        self.__date = date


class AbstractExpression(metaclass=ABCMeta):
    def interpret(self, context: Context) -> None:
        pass
