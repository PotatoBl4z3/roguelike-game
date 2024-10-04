from typing import Optional #importing Python's type hinting system

import tcod.event #importing tcod's event system

from actions import Action, EscapeAction, BumpAction #importing the Action class and its subclasses from actions.py

#Class that handles all Events
class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]: #function to quit if event is Quit. This method is overriding EventDispatch's ev_quit function
        raise SystemExit
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]: #function to check which key was pressed and return the respective action
        action: Optional[Action] = None #setting the action to None as default. This will be returned if no key press is found
        
        key = event.sym #Holds the key pressed
        
        if key == tcod.event.K_UP:
            action = BumpAction(dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx = 0, dy = 1)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
            
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
        
        #No valid key was pressed
        return action