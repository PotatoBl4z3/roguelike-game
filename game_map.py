import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int): #Game_Map constructor which takes width and height of the map
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F") #Fills the entire map with floor tiles

        self.tiles[30:33, 22] = tile_types.wall #Creates a three-wide wall at the specified location (will be removed later)

    def in_bounds(self, x: int, y: int) -> bool: 
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None: #Render function
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]