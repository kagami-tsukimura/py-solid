from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    def handle(self, user_id: str):
        pass


class RealServer(Server):
    def handle(self, user_id: str):
        print(f"RealServer: handle request for {user_id}")


class Proxy(Server):
    def __init__(self, server: Server):
        self.__server = server

    def _authorize(self, user_id: str):
        authorized_user_id = ["1", "2", "3"]
        if not user_id in authorized_user_id:
            raise Exception("Unauthorized user")

    def handle(self, user_id: str):
        self._authorize(user_id)
        self.__server.handle(user_id)

        print(f"Proxy: handle request for {user_id}")
