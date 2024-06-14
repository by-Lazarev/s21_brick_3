# tests/test_old_games.py
from fastapi.testclient import TestClient
from brick_game.server.app import app

client = TestClient(app)

def test_game_v1_start():
    response = client.post("/game_v1/start")
    assert response.status_code == 200
    assert response.json() == {"message": "Game V1 started"}

def test_game_v2_start():
    response = client.post("/game_v2/start")
    assert response.status_code == 200
    assert response.json() == {"message": "Game V2 started"}

