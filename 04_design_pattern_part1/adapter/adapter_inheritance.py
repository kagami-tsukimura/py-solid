from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


class NewLibrary:
    # return: key: str, value: strの辞書型配列
    def get_json_data(self) -> list[dict[str, str]]:
        pass
