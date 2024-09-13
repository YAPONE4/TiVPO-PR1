from typing import TextIO
from tivpo_pr1.screen_grid import ScreenGrid


class Parser:
    """Parse file to construct ScreenGrid."""

    _current_line: str
    _current_line_num: int

    _screen_grid: ScreenGrid

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
