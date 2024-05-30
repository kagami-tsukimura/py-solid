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
                member.receive(msg)


class User(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator, name: str) -> None:
        self._mediator = mediator
        self._name = name

    @abstractmethod
    def send(self, msg: str) -> None:
        pass

    @abstractmethod
    def receive(self, msg: str) -> None:
        pass


class ChatUser(User):
    def __init__(self, mediator: Mediator, name: str) -> None:
        super().__init__(mediator, name)

    def send(self, msg: str) -> None:
        print(f"{self._name} -> send message.")
        self._mediator.send_message(f"{msg} from {self._name}", self)

    def receive(self, msg: str) -> None:
        print(f"{self._name} received {msg}")


if __name__ == "__main__":
    # チャットルーム作成
    mediator = ChatRoom()

    # ユーザー作成
    user1 = ChatUser(mediator, "user1")
    user2 = ChatUser(mediator, "user2")
    user3 = ChatUser(mediator, "user3")

    # ユーザー登録
    mediator.register_user(user1)
    mediator.register_user(user2)
    mediator.register_user(user3)

    # メッセージ送信
    # Mediator によりメッセージ送信の仲介
    user1.send("hello1")
    user2.send("hello2")
    user3.send("hello3")
