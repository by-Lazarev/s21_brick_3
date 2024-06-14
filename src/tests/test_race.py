import pytest
from brick_game.race.game_logic import RacingGame, Direction
from brick_game.race.fsm import State

def test_initial_game_state():
    game = RacingGame()
    assert game.car_position == game.track_width // 2
    assert game.state.state == State.INIT

def test_move_car():
    game = RacingGame()
    game.start_game()
    initial_position = game.car_position

    game.move_car(Direction.LEFT)
    assert game.car_position == initial_position - 1
    assert game.score == 1  # Проверяем начисление очков

    game.move_car(Direction.RIGHT)
    assert game.car_position == initial_position
    assert game.score == 2  # Проверяем увеличение очков

def test_game_over_on_collision():
    game = RacingGame()
    game.start_game()
    game.opponent_cars.append((game.car_position, game.track_height - 2))

    game.update()
    assert game.state.state == State.GAME_OVER

def test_score_and_max_score():
    game = RacingGame()
    game.start_game()

    for _ in range(10):
        game.move_car(Direction.FORWARD)

    assert game.score == 10
    assert game.max_score == 10  # Проверяем, что max_score обновился

    game.reset()
    game.start_game()

    for _ in range(5):
        game.move_car(Direction.FORWARD)

    assert game.score == 5
    assert game.max_score == 10  # Проверяем, что max_score сохранился

def test_level_up():
    game = RacingGame()
    game.start_game()

    for _ in range(5):
        game.move_car(Direction.FORWARD)

    assert game.level == 2  # Уровень должен повыситься до 2
    assert game.speed_multiplier > 1  # Проверяем увеличение скорости

    for _ in range(10):
        game.move_car(Direction.FORWARD)

    assert game.level == 4  # Уровень должен повыситься до 4
    assert game.speed_multiplier > 1  # Проверяем дальнейшее увеличение скорости

