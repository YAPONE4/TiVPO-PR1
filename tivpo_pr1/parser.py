from typing import TextIO
from tivpo_pr1.screen_grid import ScreenGrid


class Parser:
    """Parse file to construct ScreenGrid."""

    @staticmethod
    def parse(file: TextIO = None) -> ScreenGrid:
        print("File parsed")
        return ScreenGrid()
