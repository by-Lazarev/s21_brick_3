from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from brick_game.race.game_logic import RacingGame, Direction
from brick_game.race.fsm import State
from brick_game.console_interface_v1.logic import GameV1  # Импортируем игру v1.0
from brick_game.desktop_interface_v2.logic import GameV2  # Импортируем игру v2.0

app = FastAPI()
game = RacingGame()
game_v1 = GameV1()  # Инициализируем игру v1.0
game_v2 = GameV2()  # Инициализируем игру v2.0

class MoveRequest(BaseModel):
    direction: Direction

# Раздача статических файлов
app.mount("/static", StaticFiles(directory="brick_game/web_gui"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("brick_game/web_gui/index.html")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/game/start")
async def start_game():
    game.start_game()
    return {"message": "Game started"}

@app.post("/game/move")
async def move_car(move: MoveRequest):
    if game.state.state != State.RUNNING:
        raise HTTPException(status_code=400, detail="Game is not running")
    game.move_car(move.direction)
    return {"message": f"Car moved {move.direction.value}"}

@app.get("/game/status")
async def get_status():
    return {
        "car_position": game.car_position,
        "opponent_cars": game.opponent_cars,
        "state": game.state.state.name,
        "score": game.score,
        "max_score": game.max_score,  # Добавляем максимальный результат
        "level": game.level  # Добавляем текущий уровень
    }

@app.post("/game/reset")
async def reset_game():
    game.reset()
    return {"message": "Game reset"}

# Добавляем маршруты для игры v1.0
@app.post("/game_v1/start")
async def start_game_v1():
    game_v1.start()
    return {"message": "Game V1 started"}

# Добавляем маршруты для игры v2.0
@app.post("/game_v2/start")
async def start_game_v2():
    game_v2.start()
    return {"message": "Game V2 started"}

