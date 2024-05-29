from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, user_id: str) -> None:
        pass


class RealServer(Server):
    def handle(self, user_id: str) -> None:
        print(f"RealServer: handle request for {user_id}")


class Proxy(Server):
    def __init__(self, server: Server) -> None:
        self.__server = server

    def _authorize(self, user_id: str) -> None:
        authorized_user_id = ["1", "2", "3"]
        if user_id not in authorized_user_id:
            raise Exception("Unauthorized user")

    def handle(self, user_id: str) -> None:
        self._authorize(user_id)

        print(f"Proxy: handle request for {user_id}")
        self.__server.handle(user_id)
        print(f"Proxy: done handling request for {user_id}")


if __name__ == "__main__":
    real_server = RealServer()
    proxy = Proxy(real_server)

    user_id = "1"
    proxy.handle(user_id)

    user_id = "3"
    proxy.handle(user_id)

    # user_id = "4"
    # proxy.handle(user_id)
