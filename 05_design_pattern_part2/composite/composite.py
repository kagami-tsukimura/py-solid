from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.__size = size

    def get_size(self) -> int:
        return self.__size

    def remove(self) -> None:
        print(f"remove file: {self.name}")


class Directory(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__children: list[Entry] = []

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.__children)

    def remove(self) -> None:
        [child.remove() for child in self.__children]
        print(f"remove directory: {self.name}")

    def add(self, entry: Entry) -> None:
        self.__children.append(entry)


def client(entry: Entry) -> None:
    print(entry.name)
    print(entry.get_size())
    entry.remove()


if __name__ == "__main__":
    composite_dir1 = Directory("design_pattern")
    composite_dir2 = Directory("composite")
    file1 = File("composite.py", 100)
    file1 = File("practice.png", 150)

    composite_dir2.add(file1)
    composite_dir1.add(composite_dir2)

    client(composite_dir1)
