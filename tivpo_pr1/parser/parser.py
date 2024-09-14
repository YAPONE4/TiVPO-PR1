from typing import TextIO
from tivpo_pr1.grid_objects.objects import GridObject
from tivpo_pr1.parser.exceptions import InvalidSymbolError
from tivpo_pr1.grid_objects import GRID_OBJECTS_MAP


class Parser:
    """Parse file to construct ScreenGrid."""

    _current_line_contents: str
    _current_line_num: int

    _parsed_objects: list[GridObject] = []

    def parse(self, file: TextIO) -> list[GridObject]:
        for line_num, line in enumerate(file):
            self._current_line_num = line_num + 1
            self._current_line_contents = line
            self._parse_line()

        return self._parsed_objects

    def _parse_line(self):
        for index, symbol in enumerate(self._current_line_contents.split()):
            if symbol in GRID_OBJECTS_MAP:
                object: GridObject = GRID_OBJECTS_MAP[symbol]()
                object.line_num = self._current_line_num
                object.index = index
                self._parsed_objects.append(object)
            else:
                # raise InvalidSymbolError(
                #     f'Unknown symbol "{symbol}" on line {self._current_line_num} at index {index}'
                # )
                pass
