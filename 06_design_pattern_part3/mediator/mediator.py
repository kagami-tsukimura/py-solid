from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def register_user(self, user: User) -> None:
        pass

    @abstractmethod
    def send_message(self, sendUser: User) -> None:
        pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.members: list[User] = []
