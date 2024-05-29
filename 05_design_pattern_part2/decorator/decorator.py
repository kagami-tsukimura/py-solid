import datetime
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):

    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class Logger(Component):

    def get_log_message(self, msg: str) -> str:
        return msg
