from abc import ABCMeta, abstractmethod


class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class LINE(MessageApp):
    def send(self, message: str) -> None:
        print(f"[LINE] {message}")


class X(MessageApp):
    def send(self, message: str) -> None:
        print(f"[X] {message}")


class Facebook(MessageApp):
    def send(self, message: str) -> None:
        print(f"[Facebook] {message}")


class OS(metaclass=ABCMeta):
    def __init__(self):
        self._app = None

    def set_app(self, app: MessageApp) -> None:
        self._app = app
