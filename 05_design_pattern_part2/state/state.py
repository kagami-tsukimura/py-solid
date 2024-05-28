from __future__ import annotations

from abc import ABCMeta, abstractmethod


class LightState(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass


class OffState(LightState):
    def switch(self) -> LightState:
        print("Light is on")
        return OnState()


class OnState(LightState):
    def switch(self) -> LightState:
        print("Light is off")
        return OffState()


class LightSwitch:
    def __init__(self) -> None:
        self.__state = OffState()

    def switch(self) -> None:
        self.__state.switch()


if __name__ == "__main__":
    light = LightSwitch()
    light.switch()
    light.switch()
