from abc import ABCMeta, abstractmethod


class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class LINE(MessageApp):
    def send(self, message: str) -> None:
        print(f"[LINE] {message}")
