from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from brick_game.race.game_logic import RacingGame, Direction
from brick_game.race.fsm import State
from pathlib import Path

app = FastAPI()
game = RacingGame()

class MoveRequest(BaseModel):
    direction: Direction

# Раздача статических файлов
app.mount("/static", StaticFiles(directory="brick_game/web_gui"), name="static")

@app.get("/")
async def read_index():
    # Возвращаем index.html как HTML файл
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
        "score": game.score
    }

@app.post("/game/reset")
async def reset_game():
    game.reset()
    return {"message": "Game reset"}
