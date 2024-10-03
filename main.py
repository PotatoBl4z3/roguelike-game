#!/usr/bin/env python3
import tcod

from actions import Action, EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80 #Setting the screen width
    screen_height = 50 #Setting the screen height
    
    player_x = int(screen_width/2) #Setting the player's x position
    player_y = int(screen_height/2) #Setting the player's y position
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    ) #Loading the tileset from the png
    
    event_handler = EventHandler()  #Creating the Event Handler object which recieves events and processes them
    
    with tcod.context.new_terminal(  #Creating a new terminal with the given values
        screen_width,
        screen_height,
        tileset=tileset,
        title="RogueLikeProject",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F") #Creating a console to which all the changes are drawn
        while True: #Game Loop
            root_console.print(x=player_x, y=player_y, string= "@") #Printing the player "@" to the console
            
            context.present(root_console) #Presenting the console to the player
            
            root_console.clear() #Clears the console after presenting
             
            for event in tcod.event.wait(): #Waiting for an event
                action = event_handler.dispatch(event) #Creating an action object
                
                if action is None: #If no action is performed 
                    continue
                
                if isinstance(action, MovementAction): #If the action performed is an instance of the MovementAction class
                    player_x += action.dx #Increment the player's x value by the given amount
                    player_y += action.dy #Increment the player's y value by the given amount
                    
                elif isinstance(action, EscapeAction): #If the action performed is an instance of the EscapeAction class
                    raise SystemExit()


if __name__ == "__main__":
    main()