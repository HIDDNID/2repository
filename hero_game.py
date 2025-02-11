class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

    def player_turn(self):
        action = input("Введите 'attack' для атаки: ")
        if action.lower() == 'attack':
            self.player.attack(self.computer)
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
        else:
            print("Неверная команда!")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"Здоровье {self.player.name}: {self.player.health}")


if __name__ == "__main__":
    game = Game()
    game.start()
