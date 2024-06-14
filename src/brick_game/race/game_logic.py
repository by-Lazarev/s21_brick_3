from enum import Enum, auto
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
        self.max_score = 0
        self.level = 1
        self.max_level = 10
        self.level_up_score = 5  # Очки, необходимые для повышения уровня
        self.speed_multiplier = 1  # Коэффициент увеличения скорости
        self.load_max_score()

    def start_game(self):
        self.state.transition('start')
        self.score = 0
        self.level = 1
        self.speed_multiplier = 1

    def move_car(self, direction: Direction):
        if self.state.state == State.RUNNING:
            if direction == Direction.LEFT and self.car_position > 0:
                self.car_position -= 1
            elif direction == Direction.RIGHT and self.car_position < self.track_width - 1:
                self.car_position += 1

            self.score += 1
            self.update_level()
            self.update_max_score()

    def update(self):
        if self.state.state == State.RUNNING:
            self.opponent_cars = [(x, y + self.speed_multiplier) for x, y in self.opponent_cars if y + self.speed_multiplier < self.track_height]

            if any(y == self.track_height - 1 and x == self.car_position for x, y in self.opponent_cars):
                self.state.transition('game_over')

            import random
            if random.random() < 0.1:
                self.opponent_cars.append((random.randint(0, self.track_width - 1), 0))

            self.score += 1
            self.update_level()
            self.update_max_score()

    def reset(self):
        self.__init__()

    def update_level(self):
        # Обновляем уровень игры в зависимости от очков
        if self.score >= self.level * self.level_up_score and self.level < self.max_level:
            self.level += 1
            self.speed_multiplier += 0.1  # Увеличиваем скорость с каждым уровнем

    def update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            self.save_max_score()

    def save_max_score(self):
        with open("max_score.json", "w") as f:
            import json
            json.dump({"max_score": self.max_score}, f)

    def load_max_score(self):
        try:
            with open("max_score.json", "r") as f:
                import json
                data = json.load(f)
                self.max_score = data.get("max_score", 0)
        except FileNotFoundError:
            self.max_score = 0

