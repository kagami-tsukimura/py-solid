from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def register_user(self, user: User) -> None:
        pass

    @abstractmethod
    def send_message(self, send_user: User) -> None:
        pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.__members: list[User] = []

    def register_user(self, user: User) -> None:
        self.__members.append(user)

    def send_message(self, msg: str, send_user: User) -> None:
        for member in self.__members:
            # 本人以外に送信
            if member != send_user:
                member.receive(msg, send_user)


class User(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator, name: str) -> None:
        self.__mediator = mediator
        self.__name = name

    def receive(self, msg: str, send_user: User) -> None:
        print(f"[{self.__name}]: {msg} from {send_user.__name}")
