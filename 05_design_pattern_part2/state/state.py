from __future__ import annotations

from abc import ABCMeta, abstractmethod


class LightState(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass
