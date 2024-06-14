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

    game.move_car(Direction.RIGHT)
    assert game.car_position == initial_position

def test_game_over_on_collision():
    game = RacingGame()
    game.start_game()
    game.opponent_cars.append((game.car_position, game.track_height - 2))

    game.update()
    assert game.state.state == State.GAME_OVER

