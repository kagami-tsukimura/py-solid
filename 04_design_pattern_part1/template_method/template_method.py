from abc import ABCMeta, abstractmethod


class TestTemplate(metaclass=ABCMeta):
    def test(self) -> None:
        self.setup()
        self.execute()
        self.teardown()

    def setup(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def teardown() -> None:
        pass
