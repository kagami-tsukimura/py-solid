from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    def handle(self, user_id: str):
        pass
