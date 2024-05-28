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


class NotNullValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        print(f"NotNullValidationHandler: {bool(input)}")
        return bool(input)

    def _get_error_message(self) -> None:
        print("入力値を入力してください。")


class AlphabetValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        print(f"AlphabetValidationHandler: {re.match('^[a-zA-Z]+$', input)}")
        return re.match("[a-zA-Z]+$", input)

    def _get_error_message(self) -> None:
        print("英字のみを入力してください。")


class MinLengthValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        print(f"MinLengthValidationHandler: {len(input) >= 8}")
        return len(input) >= 8

    def _get_error_message(self) -> None:
        print("最低8文字以上を入力してください。")


if __name__ == "__main__":
    not_null = NotNullValidationHandler()
    alphabet = AlphabetValidationHandler()
    min_length = MinLengthValidationHandler()
    not_null.set_handler(alphabet)
    not_null.set_handler(min_length)
    not_null.validate("hoge")
    min_length.validate("h123456oge")
