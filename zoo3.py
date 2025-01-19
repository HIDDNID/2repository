import json


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def to_dict(self):
        return {"name": self.name, "species": self.species, "age": self.age}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['species'], data['age'])

    def __str__(self):
        return f"{self.name} - {self.species}, Age: {self.age}"


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def to_dict(self):
        return {"name": self.name, "position": self.position}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['position'])

    def __str__(self):
        return f"{self.name} - Position: {self.position}"


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name} the {animal.species}.")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name} the {animal.species}.")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, name, species, age):
        new_animal = Animal(name, species, age)
        self.animals.append(new_animal)
        print(f"Animal added: {new_animal}")

    def add_employee(self, name, position):
        if position.lower() == "zookeeper":
            new_employee = ZooKeeper(name, position)
        elif position.lower() == "veterinarian":
            new_employee = Veterinarian(name, position)
        else:
            new_employee = Employee(name, position)

        self.employees.append(new_employee)
        print(f"Employee added: {new_employee}")

    def show_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def show_employees(self):
        print("Employees in the zoo:")
        for employee in self.employees:
            print(employee)

    def save_to_file(self, filename):
        data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "employees": [employee.to_dict() for employee in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.animals = [Animal.from_dict(animal) for animal in data.get("animals", [])]
                self.employees = [Employee.from_dict(employee) for employee in data.get("employees", [])]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("File not found. Starting with an empty zoo.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty zoo.")


def main():
    zoo = Zoo()

    # Загружаем данные из файла при старте программы
    zoo.load_from_file("zoo_data.json")

    while True:
        action = input(
            "Choose an action: (1) Add Animal (2) Add Employee (3) Show Animals (4) Show Employees (5) Feed Animal (6) Heal Animal (7) Save (8) Exit: ")

        if action == '1':
            name = input("Enter animal's name: ")
            species = input("Enter animal's species: ")
            age = int(input("Enter animal's age: "))
            zoo.add_animal(name, species, age)

        elif action == '2':
            name = input("Enter employee's name: ")
            position = input("Enter employee's position (Zookeeper/Veterinarian): ")
            zoo.add_employee(name, position)

        elif action == '3':
            zoo.show_animals()

        elif action == '4':
            zoo.show_employees()

        elif action == '5':
            employee_name = input("Enter the zookeeper's name: ")
            animal_name = input("Enter the animal's name to feed: ")
            employee = next((e for e in zoo.employees if e.name == employee_name and isinstance(e, ZooKeeper)), None)
            animal = next((a for a in zoo.animals if a.name == animal_name), None)

            if employee and animal:
                employee.feed_animal(animal)
            else:
                print("Invalid zookeeper or animal name.")

        elif action == '6':
            employee_name = input("Enter the veterinarian's name: ")
            animal_name = input("Enter the animal's name to heal: ")
            employee = next((e for e in zoo.employees if e.name == employee_name and isinstance(e, Veterinarian)), None)
            animal = next((a for a in zoo.animals if a.name == animal_name), None)

            if employee and animal:
                employee.heal_animal(animal)
            else:
                print("Invalid veterinarian or animal name.")

        elif action == '7':
            zoo.save_to_file("zoo_data.json")

        elif action == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

    if __name__ == "__main__":
        main()
