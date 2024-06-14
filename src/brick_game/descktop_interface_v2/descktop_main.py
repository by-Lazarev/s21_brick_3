import tkinter as tk
import requests

class DesktopInterface:
    def __init__(self, root):
        self.api_url = "http://127.0.0.1:8000"
        self.root = root
        self.root.title("Racing Game")

        self.status_label = tk.Label(root, text="Нажмите 'Start Game' для начала.")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=5)

        self.left_button = tk.Button(root, text="Move Left", command=lambda: self.move_car("left"))
        self.left_button.pack(pady=5)

        self.right_button = tk.Button(root, text="Move Right", command=lambda: self.move_car("right"))
        self.right_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def start_game(self):
        response = requests.post(f"{self.api_url}/game/start")
        self.status_label.config(text=response.json()["message"])

    def move_car(self, direction):
        response = requests.post(f"{self.api_url}/game/move", json={"direction": direction})
        self.status_label.config(text=response.json()["message"])

    def reset_game(self):
        response = requests.post(f"{self.api_url}/game/reset")
        self.status_label.config(text=response.json()["message"])

if __name__ == "__main__":
    root = tk.Tk()
    interface = DesktopInterface(root)
    root.mainloop()
