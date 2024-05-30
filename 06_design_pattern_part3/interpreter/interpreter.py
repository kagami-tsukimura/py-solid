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

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        year = context.date.year
        context.expression = expression.replace("YYYY", str(year))

        if self.__child:
            self.__child.interpret(context)

        return context


class MonthExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        month = context.date.month
        # zfill(2): 1桁の月を2桁に変換
        context.expression = expression.replace("MM", str(month).zfill(2))

        if self.__child:
            self.__child.interpret(context)

        return context


class DayExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        day = context.date.day
        # zfill(2): 1桁の月を2桁に変換
        context.expression = expression.replace("DD", str(day).zfill(2))

        if self.__child:
            self.__child.interpret(context)

        return context


if __name__ == "__main__":
    now_date = datetime.datetime.now().date()
    expression = "MM/DD/YYYY"
    context = Context(expression, now_date)
    year = YearExpression()
    month = MonthExpression()
    day = DayExpression()

    year.set_child(month)
    month.set_child(day)

    year.interpret(context)
    print(context.expression)
