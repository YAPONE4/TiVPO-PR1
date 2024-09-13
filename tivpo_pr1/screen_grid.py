from tivpo_pr1.grid_object import GridObject

class ScreenGrid:
    """Grid that was read from the file and should be drawn on the screen."""

    _screen_grid: list[list[GridObject]]

    def __init__(self):
        print("ScreenGrid createad")
