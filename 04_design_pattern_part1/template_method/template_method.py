from abc import ABCMeta, abstractmethod


class TestTemplate(metaclass=ABCMeta):
    @abstractmethod
    def test(self) -> None:
        pass

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def teardown() -> None:
        pass
