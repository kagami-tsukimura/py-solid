from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


class NewLibrary:
    # return: key: str, value: strの辞書型配列
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            {"key1": "json1", "key2": "json2"},
            {"key3": "json3", "key4": "json4"},
            {"key5": "json5", "key6": "json6"},
        ]


class JsonToCsvAdapter(Target):
    def __init__(self, adaptee: NewLibrary) -> None:
        self.__adaptee = adaptee

    def get_csv_data(self) -> str:
        json_data = self.__adaptee.get_json_data()

        # keyをカンマ区切りで取得
        header = ",".join(list(json_data[0].keys())) + "\n"
        body = "\n".join([",".join(list(d.values())) for d in json_data])

        return header + body


if __name__ == "__main__":
    adaptee = NewLibrary()
    print("---adaptee---")
    print(adaptee.get_json_data())

    adapter = JsonToCsvAdapter()
    print("---adapter---")
    print(adapter.get_csv_data())
