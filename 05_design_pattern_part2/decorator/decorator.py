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

    def __init__(self, component: Component):
        super().__init__(component)

    def get_log_message(self, msg: str) -> str:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return self._component.get_log_message(f"[{timestamp}]: {msg}")


class LogLevelDecorator(Decorator):

    def __init__(self, component: Component, log_level: str):
        super().__init__(component)
        self.__log_level = log_level

    def get_log_message(self, msg: str) -> str:
        level = self.__log_level
        return self._component.get_log_message(f"[{level}]: {msg}")
