from abc import ABCMeta, abstractmethod


class Patient:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class IIterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Patient:
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self) -> IIterator:
        pass


class WaitingRoom(Aggregate):
    def __init__(self):
        self.__patients = []

    def get_patients(self) -> list[Patient]:
        return self.__patients

    def get_count(self) -> int:
        return len(self.__patients)

    def check_in(self, patient: Patient) -> None:
        self.__patients.append(patient)

    def get_iterator(self) -> IIterator:
        return WaitingRoomIterator(self)


class WaitingRoomIterator(IIterator):
    def __init__(self, aggregate: WaitingRoom) -> None:
        self.__position = 0
        self.__aggregate = aggregate

    def has_next(self) -> bool:
        return self.__position < len(self.__aggregate.get_count())

    def next(self) -> Patient:
        if not self.has_next():
            print("患者がいません")
            return

        patient = self.__aggregate.get_patients()[self.__position]
        self.__position += 1

        return patient


if __name__ == "__main__":
    waiting_room = WaitingRoom()

    waiting_room.check_in(Patient(1, "Taro"))
    waiting_room.check_in(Patient(2, "Jiro"))
    waiting_room.check_in(Patient(3, "Hanako"))

    for patient in waiting_room.get_iterator():
        print(patient)
