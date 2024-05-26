from abc import ABCMeta, abstractmethod


class Patient:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"
