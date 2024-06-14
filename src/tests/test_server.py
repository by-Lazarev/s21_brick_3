from fastapi.testclient import TestClient
from brick_game.server.app import app

client = TestClient(app)

def test_start_game():
    response = client.post("/game/start")
    assert response.status_code == 200
    assert response.json() == {"message": "Game started"}

def test_move_car():
    client.post("/game/start")
    response = client.post("/game/move", json={"direction": "left"})
    assert response.status_code == 200
    assert response.json() == {"message": "Car moved left"}

def test_get_status():
    client.post("/game/start")
    response = client.get("/game/status")
    assert response.status_code == 200
    status = response.json()
    assert "car_position" in status
    assert "opponent_cars" in status
    assert "state" in status
    assert "score" in status

def test_reset_game():
    response = client.post("/game/reset")
    assert response.status_code == 200
    assert response.json() == {"message": "Game reset"}

