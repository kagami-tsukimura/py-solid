from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    def handle(self, user_id: str):
        pass


class RealServer(Server):
    def handle(self, user_id: str):
        print(f"RealServer: handle request for {user_id}")
