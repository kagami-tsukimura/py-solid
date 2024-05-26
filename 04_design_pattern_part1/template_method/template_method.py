from abc import ABCMeta, abstractmethod


class TestTemplate(metaclass=ABCMeta):
    def test(self) -> None:
        self.setup()
        self.execute()
        self.teardown()

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    def teardown(self) -> None:
        print("teardown")
