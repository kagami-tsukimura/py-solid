import datetime


class Logger:
    # クラス変数
    _instance = None

    # インスタンス生成のために作成（インスタンス生成前に実行）
    def __new__(cls):
        if cls._instance is None:
            # インスタンス生成
            cls._instance = super().__new__(cls)
        return cls._instance

    def output(self, content: str) -> None:
        now = datetime.datetime.now()
        print(f"[{now}]: {content}")
