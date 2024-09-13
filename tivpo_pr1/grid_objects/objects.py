from abc import ABC


class GridObject(ABC):
    """Singular item of the ScreenGrid."""

    symbol: str


class RightArrow(GridObject):
    symbol = "->"


class LeftArrow(GridObject):
    symbol = "<-"


class LeftRightArrow(GridObject):
    symbol = "<->"


class Sircle(GridObject):
    symbol = "()"


class Square(GridObject):
    symbol = "[]"
