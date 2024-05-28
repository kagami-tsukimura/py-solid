# 自身のクラスを引数にして、継承しているクラスのメソッドを実行できるようにする
from __future__ import annotations

import re
from abc import ABCMeta, abstractmethod


class ValidationHandler(metaclass=ABCMeta):
    def __init__(self):
        self.__next_handler = None

    def set_handler(self, handler: ValidationHandler) -> None:
        self.__next_handler = handler
        # メソッドチェイン
        return handler

    @abstractmethod
    def _exec_validation(self, input: str) -> bool:
        pass

    @abstractmethod
    def _get_error_message(self) -> None:
        pass

    def validate(self, input: str) -> bool:
        result = self._exec_validation(input)
        if not result:
            self._get_error_message()
            return False
        elif self.__next_handler:
            # handlerがなくなるまで処理を繰り返す
            return self.__next_handler.validate(input)
        else:
            return True
