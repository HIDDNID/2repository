class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Общие методы для всех животных
    def make_sound(self):
        raise NotImplementedError("Метод make_sound должен быть реализован в подклассах")

    def eat(self):
        print(f"{self.name}, возраст {self.age}, ест пищу.")


# Подклассы наследуют от базового класса Animal
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, лает: Гав!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, мяукает: Мяу!")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name}, возраст {self.age}, чирикает: Чирик-чирик!")


# Создание объектов различных классов
dog = Dog("Шарик", 4)
cat = Cat("Васька", 2)
bird = Bird("Кеша", 1)

# Вызов методов через полиморфизм
animals = [dog, cat, bird]
for animal in animals:
    animal.make_sound()
    animal.eat()
