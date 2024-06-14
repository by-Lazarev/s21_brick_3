import requests
import sys

class ConsoleInterface:
    def __init__(self):
        self.api_url = "http://127.0.0.1:8000"

    def start_game(self):
        response = requests.post(f"{self.api_url}/game/start")
        print(response.json())

    def move_car(self, direction):
        response = requests.post(f"{self.api_url}/game/move", json={"direction": direction})
        print(response.json())

    def reset_game(self):
        response = requests.post(f"{self.api_url}/game/reset")
        print(response.json())

    def get_status(self):
        response = requests.get(f"{self.api_url}/game/status")
        print(response.json())

    def run(self):
        print("Консольный интерфейс для игры 'Гонки'")
        while True:
            command = input("Введите команду (start, left, right, reset, status, exit): ").strip().lower()
            if command == 'start':
                self.start_game()
            elif command == 'left':
                self.move_car('left')
            elif command == 'right':
                self.move_car('right')
            elif command == 'reset':
                self.reset_game()
            elif command == 'status':
                self.get_status()
            elif command == 'exit':
                print("Выход из игры.")
                break
            else:
                print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    interface = ConsoleInterface()
    interface.run()

