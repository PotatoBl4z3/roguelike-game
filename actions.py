class Action:
    pass


class EscapeAction(Action):
    pass

class MovementAction(Action):
    def __init__(self, dx: int, dy: int): #Constructor (????) idk im trying to learn Python OOP
        super().__init__()
        
        self.dx = dx #self is kinda like this in Java ig
        self.dy = dy