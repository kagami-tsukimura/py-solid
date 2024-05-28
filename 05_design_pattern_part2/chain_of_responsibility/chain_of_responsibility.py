# 自身のクラスを引数にして、継承しているクラスのメソッドを実行できるようにする
from __future__ import annotations

import re
from abc import ABCMeta, abstractmethod


class ValidationHandler(metaclass=ABCMeta):
    def __init__(self):
        self.__next_handler = None
