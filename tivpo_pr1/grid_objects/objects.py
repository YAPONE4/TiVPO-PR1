from abc import ABC


class GridObject(ABC):
    """Singular item of the ScreenGrid."""

    symbol: str = None
    line_num: int = None
    index: int = None


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
