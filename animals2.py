class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound должен быть реализован в подклассах")

    def eat(self):
        print(f"{self.name}, возраст {self.age}, ест пищу.")


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        if self.can_fly:
            if self.name == "Ворона":
                print(f"{self.name}, возраст {self.age}, каркает: Карр-карр!")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, has_hair=True):
        super().__init__(name, age)
        self.has_hair = has_hair

    def make_sound(self):
        if self.has_hair:
            print(f"{self.name}, возраст {self.age}, фыркает: Ф-ф-ф!")


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, is_cold_blooded=True):
        super().__init__(name, age)
        self.is_cold_blooded = is_cold_blooded

    def make_sound(self):
        if self.is_cold_blooded:
            print(f"{self.name}, возраст {self.age}, шипит: Ш-ш-ш!")
        else:
            print(f"{self.name}, возраст {self.age}, квакает: Ква-ква!")


# Создание объектов конкретных видов животных
crow = Bird("Ворона", 3, True)
elephant = Mammal("Слон", 10)
crocodile = Reptile("Крокодил", 20)

# Вызов методов через полиморфизм
animals = [crow, elephant, crocodile]
for animal in animals:
    animal.make_sound()
    animal.eat()
