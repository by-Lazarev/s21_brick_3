# brick_game/console_interface_v1/logic.py

class GameV1:
    def __init__(self):
        self.state = "initialized"
        print("Game V1 initialized")

    def start(self):
        self.state = "started"
        print("Game V1 started")

    def update(self):
        print("Game V1 updated")

    def reset(self):
        self.state = "reset"
        print("Game V1 reset")

