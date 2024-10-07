#!/usr/bin/env python3
import copy
import tcod

import color
import entity_factories
from procgen import RectangularRoom
from engine import Engine


def main() -> None:
    screen_width = 80 #Setting the screen width
    screen_height = 50 #Setting the screen height
    
    map_width = 80 #Setting the map width
    map_height = 43 #Setting the map height
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    max_monsters_per_room = 2
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    ) #Loading the tileset from the png
    
    player = copy.deepcopy(entity_factories.player) #Creating a Player entity
    
    engine = Engine(player=player)
    
    engine.game_map = RectangularRoom.generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    ) #Creating the game map (P.S. its not working without importing RectangularRoom so idk come back to this later)
    
    engine.update_fov()
    
    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )
    
    with tcod.context.new_terminal(  #Creating a new terminal with the given values
        screen_width,
        screen_height,
        tileset=tileset,
        title="RogueLikeProject",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F") #Creating a console to which all the changes are drawn
        while True: #Game Loop
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            
            engine.event_handler.handle_events(context)


if __name__ == "__main__":
    main()