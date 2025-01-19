class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound должен быть реализован в подклассах")

    def eat(self):
        print(f"{self.name}, возраст {self.age}, ест пищу.")


# Подкласс Cat
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, мяукает: Мяу!")


# Подкласс Dog
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, лает: Гав!")


# Подкласс Lion
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, рычит: Р-р-р!")


# Подкласс Frog
class Frog(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, квакает: Ква-ква!")


# Подкласс Owl
class Owl(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, ухает: У-ху!")


# Функция для вызова звука у списка животных
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Список животных для выбора
animals_list = [
    ("кошка", Cat("Мурка", 2)),
    ("собака", Dog("Бобик", 3)),
    ("лев", Lion("Царь зверей", 7)),
    ("лягушка", Frog("Кваки", 1)),
    ("сова", Owl("Ухти-Тухти", 5))
]

# Основная логика программы
if __name__ == "__main__":
    while True:
        print("\nДоступные животные:")
        for i, (animal_name, _) in enumerate(animals_list):
            print(f"{i + 1}. {animal_name}")

        try:
            choice = int(input("\nВведите номер животного, чтобы узнать его звук: "))
            if 0 < choice <= len(animals_list):
                _, animal = animals_list[choice - 1]
                animal.make_sound()
            else:
                print("Неверный ввод. Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода. Вводить нужно число.")
