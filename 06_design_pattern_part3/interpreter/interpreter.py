import datetime
import re
from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):
    def interpret(self, context: Context) -> None:
        pass
