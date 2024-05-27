from abc import ABCMeta, abstractmethod


class Computer:
    def __init__(self):
        self.type = None
        self.cpu = None
        self.ram = None

    def __str__(self):
        return f"{self.type} {self.cpu} {self.ram}"
