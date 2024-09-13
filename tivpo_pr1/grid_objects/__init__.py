import sys, inspect
from . import objects
from .objects import GridObject


def _generate_grid_objects_map() -> dict[str, GridObject]:
    grid_objects: dict[str, GridObject] = []
    for name, cls in inspect.getmembers(objects):
        if inspect.isclass(cls) and issubclass(cls, GridObject) and cls is not GridObject:
            grid_objects.ap
    return grid_objects
