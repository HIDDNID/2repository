from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass

class Sword(Weapon):
    def attack(self, target):
        print(f"Боец атаковал мечом и нанес {20} процентов урона.")
        target.take_damage(20)

class Bow(Weapon):
    def attack(self, target):
        print(f"Боец выстрелил из лука и нанес {15} процентов урона.")
        target.take_damage(15)

class Fighter:
    def __init__(self, weapon=None):
        self.health = 100
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self, monster):
        if self.weapon is not None:
            self.weapon.attack(monster)
        else:
            print("У бойца нет оружия!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Боец погиб...")

class Monster:
    def __init__(self, health=50, strength=10):
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Монстр повержен!")

    def attack(self, fighter):
        print(f"Монстр атаковал и нанес {self.strength} процентов урона.")
        fighter.take_damage(self.strength)

def battle(fighter, monster):
    while True:
        fighter.attack(monster)
        if monster.health <= 0:
            break

        monster.attack(fighter)
        if fighter.health <= 0:
            break


if __name__ == "__main__":
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster()

    print("Начало битвы!")
    battle(fighter, monster)

    # Меняем оружие бойца на лук
    fighter.change_weapon(bow)
    monster = Monster()

    print("\nНовая битва!")
    battle(fighter, monster)

    print("Битвы завершены!")
