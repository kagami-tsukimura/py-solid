from abc import ABCMeta, abstractmethod


class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass
