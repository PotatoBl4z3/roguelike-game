from __future__ import annotations

from typing import Optional, TYPE_CHECKING #importing Python's type hinting system

import tcod.event #importing tcod's event system

from actions import Action, EscapeAction, BumpAction #importing the Action class and its subclasses from actions.py

if TYPE_CHECKING:
    from engine import Engine

#Class that handles all Events
class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()  # Update the FOV before the players next action.
            
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]: #function to quit if event is Quit. This method is overriding EventDispatch's ev_quit function
        raise SystemExit
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]: #function to check which key was pressed and return the respective action
        action: Optional[Action] = None #setting the action to None as default. This will be returned if no key press is found
        
        key = event.sym #Holds the key pressed
        
        player = self.engine.player
        
        if key == tcod.event.K_UP:
            action = BumpAction(player, dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(player, dx = 0, dy = 1)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(player, dx=1, dy=0)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(player, dx=-1, dy=0)
            
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)
        
        #No valid key was pressed
        return action