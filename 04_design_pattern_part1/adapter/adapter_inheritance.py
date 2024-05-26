from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass
