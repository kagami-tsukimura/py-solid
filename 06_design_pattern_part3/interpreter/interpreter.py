import datetime
import re
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, expression: str, date: datetime.date):
        self.validate(expression)
        self.expression = expression
        self.date = date

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
        expression = context.expression
        year = context.date.year
        context.expression = expression.replace("YYYY", str(year))

        if self.__child:
            self.__child.interpret(context)
