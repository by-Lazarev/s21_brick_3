from enum import Enum, auto

class State(Enum):
    INIT = auto()
    RUNNING = auto()
    PAUSED = auto()
    GAME_OVER = auto()

class FSM:
    def __init__(self):
        self.state = State.INIT

    def transition(self, event):
        if self.state == State.INIT and event == 'start':
            self.state = State.RUNNING
        elif self.state == State.RUNNING and event == 'pause':
            self.state = State.PAUSED
        elif self.state == State.PAUSED and event == 'resume':
            self.state = State.RUNNING
        elif self.state == State.RUNNING and event == 'game_over':
            self.state = State.GAME_OVER
        elif self.state == State.GAME_OVER and event == 'reset':
            self.state = State.INIT

