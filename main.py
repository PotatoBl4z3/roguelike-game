#!/usr/bin/env python3
import tcod

from entity import Entity
from input_handlers import EventHandler
from procgen import RectangularRoom
from engine import Engine


def main() -> None:
    screen_width = 80 #Setting the screen width
    screen_height = 50 #Setting the screen height
    
    map_width = 80 #Setting the map width
    map_height = 45 #Setting the map height
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    ) #Loading the tileset from the png
    
    event_handler = EventHandler()  #Creating the Event Handler object which recieves events and processes them
    
    player = Entity(int(screen_width/2), int(screen_height/2), "@", [255, 255, 255]) #Creating a Player entity
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0)) #Creating an NPC entity
    entities = {npc, player} #Creating a Set of entities
    
    game_map = RectangularRoom.generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    ) #Creating the game map (P.S. its not working without importing RectangularRoom so idk come back to this later)
    
    engine = Engine(entities=entities, event_handler=event_handler,game_map = game_map, player=player) #Creating the engine that handles events and rendering
    
    with tcod.context.new_terminal(  #Creating a new terminal with the given values
        screen_width,
        screen_height,
        tileset=tileset,
        title="RogueLikeProject",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F") #Creating a console to which all the changes are drawn
        while True: #Game Loop
            engine.render(console=root_console, context=context) #Calling engine's render function
            
            events = tcod.event.wait() #Inputting the event
            engine.handle_events(events=events) #Calling engine's handle events function to handle the events


if __name__ == "__main__":
    main()