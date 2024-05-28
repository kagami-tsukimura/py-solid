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
    def __init__(self, state: LightState) -> None:
        self.state = state

    def switch(self) -> None:
        self.state.switch()


if __name__ == "__main__":
    light = LightSwitch(OffState())
    light.switch()
    light.switch()
