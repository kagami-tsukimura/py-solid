import datetime
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):

    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class Logger(Component):

    def get_log_message(self, msg: str) -> str:
        return msg


class Decorator(Component):

    def __init__(self, component: Component) -> None:
        self._component = component

    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class TimestampDecorator(Decorator):

    def get_log_message(self, msg: str) -> str:
        return f"{datetime.datetime.now()}: {msg}"
