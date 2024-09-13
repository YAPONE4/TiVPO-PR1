from typing import TextIO
from tivpo_pr1.screen_grid import ScreenGrid
from tivpo_pr1.grid_objects import GRID_OBJECTS_MAP

class Parser:
    """Parse file to construct ScreenGrid."""

    _current_line: str
    _current_line_num: int

    _screen_grid: ScreenGrid

    def __init__(self) -> None:
        print(GRID_OBJECTS_MAP)


    def parse(self, file: TextIO) -> ScreenGrid:
        for line_num, line in enumerate(file):
            self._current_line_num = line_num + 1
            self._current_line = line

            self._parse_line()

        return ScreenGrid()

    def _parse_line(self):
        line_symbols: list[str] = self._current_line.split()

        for symbol in line_symbols:
            pass
