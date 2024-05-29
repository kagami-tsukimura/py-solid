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

    def get_log_message(self, msg: str) -> str:
        return self._component.get_log_message(msg)
