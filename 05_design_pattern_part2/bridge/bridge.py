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

    @abstractmethod
    def send_message(self) -> None:
        pass


class IOS(OS):
    def send_message(self) -> None:
        if self._app:
            self._app.send("Hello, iOS")
        else:
            raise Exception("App is not set")


class Android(OS):
    def send_message(self) -> None:
        if self._app:
            self._app.send("Hello, Android")
        else:
            raise Exception("App is not set")


if __name__ == "__main__":
    ios = IOS()
    ios.set_app(LINE())
    ios.send_message()

    android = Android()
    android.set_app(X())
    android.send_message()
