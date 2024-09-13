import sys, inspect
from . import objects
from .objects import GridObject


def _generate_grid_objects_map() -> dict[str, GridObject]:
    """Generate a dictionary of symbols and their classes.

    This function reads all classes in objects.py file.
    Every class that is a child of GridObject is interpreted as a GridObject
    that can be drawn to the screen.
    """
    grid_objects: dict[str, GridObject] = {}
    for name, cls in inspect.getmembers(objects):
        if (
            inspect.isclass(cls)
            and issubclass(cls, GridObject)
            and cls is not GridObject
        ):
            grid_objects[cls().symbol] = cls
    return grid_objects


GRID_OBJECTS_MAP: dict[str, GridObject] = _generate_grid_objects_map()
