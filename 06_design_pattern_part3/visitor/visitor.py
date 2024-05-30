from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    def __init__(self, code: str, name: str) -> None:
        self.__code = code
        self.__name = name
