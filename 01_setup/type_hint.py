from typing import Literal

a: int = 1
b: float
c: str
d: bool

# Python >= 3.9
e: list[int] = [1, 2, 3]
f: dict[str, bool] = {"foo": True, "bar": False}

# Literal: Enumのように使用可能 + 引数値のチェックに使用可能
g: Literal["OK", "NG"] = "OK"


def sample(x: str) -> bool:
    if x == "OK":
        return True
    return False
