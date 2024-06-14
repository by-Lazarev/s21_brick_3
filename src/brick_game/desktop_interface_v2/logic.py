# brick_game/descktop_interface_v2/logic.py

class GameV2:
    def __init__(self):
        self.state = "initialized"
        print("Game V2 initialized")

    def start(self):
        self.state = "started"
        print("Game V2 started")

    def update(self):
        print("Game V2 updated")

    def reset(self):
        self.state = "reset"
        print("Game V2 reset")

