from enum import Enum
from brick_game.race.fsm import FSM, State  

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"

class RacingGame:
    def __init__(self):
        self.track_width = 10
        self.track_height = 20
        self.car_position = self.track_width // 2
        self.opponent_cars = []
        self.state = FSM()
        self.score = 0

    def start_game(self):
        self.state.transition('start')

    def move_car(self, direction: Direction):
        if self.state.state == State.RUNNING:
            if direction == Direction.LEFT and self.car_position > 0:
                self.car_position -= 1
            elif direction == Direction.RIGHT and self.car_position < self.track_width - 1:
                self.car_position += 1

    def update(self):
        if self.state.state == State.RUNNING:
            self.opponent_cars = [(x, y + 1) for x, y in self.opponent_cars if y + 1 < self.track_height]

            if any(y == self.track_height - 1 and x == self.car_position for x, y in self.opponent_cars):
                self.state.transition('game_over')

            import random
            if random.random() < 0.1:
                self.opponent_cars.append((random.randint(0, self.track_width - 1), 0))

            self.score += 1

    def reset(self):
        self.__init__()

