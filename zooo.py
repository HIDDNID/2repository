import sqlite3

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_sick = False  # Добавляем флаг болезни

class Employee:
    def __init__(self, name, employee_type):
        self.name = name
        self.employee_type = employee_type

class Zookeeper(Employee):
    def __init__(self, name):
        super().__init__(name, 'zookeeper')

    def feed_animal(self, animal):
        print(f"{self.name} покормил(а) {animal.name}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, 'veterinarian')

    def treat_animal(self, animal):
        if animal.is_sick:
            animal.is_sick = False
            print(f"{self.name} вылечил(а) {animal.name}.")
        else:
            print(f"{animal.name} здоров(а) и не нуждается в лечении.")

class Zoo:
    def __init__(self):
        self.conn = sqlite3.connect('zoo.db')
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                species TEXT,
                is_sick BOOLEAN DEFAULT FALSE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                employee_type TEXT
            )
        ''')

        self.conn.commit()

    def add_animal(self, animal):
        self.cursor.execute('''
            INSERT INTO animals (name, species) VALUES (?, ?)
        ''', (animal.name, animal.species))
        self.conn.commit()

    def add_employee(self, employee):
        self.cursor.execute('''
            INSERT INTO employees (name, employee_type) VALUES (?, ?)
        ''', (employee.name, employee.employee_type))
        self.conn.commit()

    def get_all_animals(self):
        self.cursor.execute('''
            SELECT * FROM animals
        ''')
        return self.cursor.fetchall()

    def get_all_employees(self):
        self.cursor.execute('''
            SELECT * FROM employees
        ''')
        return self.cursor.fetchall()

    def perform_action(self, action, employee, animal):
        if action == 'feed':
            if isinstance(employee, Zookeeper):
                employee.feed_animal(animal)
            else:
                print(f"{employee.name} не может кормить животных.")
        elif action == 'treat':
            if isinstance(employee, Veterinarian):
                employee.treat_animal(animal)
            else:
                print(f"{employee.name} не может лечить животных.")
        else:
            print("Недопустимое действие.")

    def close_connection(self):
        self.conn.close()

# Основная часть программы
def main():
    zoo = Zoo()

    while True:
        print("""
        Меню:
        1. Добавить животное
        2. Добавить сотрудника
        3. Покормить животное
        4. Лечить животное
        5. Показать всех животных
        6. Показать всех сотрудников
        7. Закрыть соединение с базой данных
        8. Выход
        """)

        choice = input("Ваш выбор: ")

        if choice == '1':
            name = input("Введите имя животного: ")
            species = input("Введите вид животного: ")
            animal = Animal(name, species)
            zoo.add_animal(animal)
            print(f"Животное {name} успешно добавлено!")

        elif choice == '2':
            name = input("Введите имя сотрудника: ")
            employee_type = input("Введите тип сотрудника (zookeeper/veterinarian): ")
            if employee_type == 'zookeeper':
                employee = Zookeeper(name)
            elif employee_type == 'veterinarian':
                employee = Veterinarian(name)
            else:
                print("Неизвестный тип сотрудника!")
                continue
            zoo.add_employee(employee)
            print(f"Сотрудник {name} успешно добавлен!")

        elif choice == '3':
            animals = zoo.get_all_animals()
            employees = zoo.get_all_employees()

            if not animals or not employees:
                print("Сначала добавьте хотя бы одного сотрудника и одно животное.")
                continue

            for i, animal in enumerate(animals):
                print(f"{i+1}. Имя: {animal[1]}, Вид: {animal[2]}")

            animal_index = int(input("Выберите животное для кормления: "))
            selected_animal = Animal(animals[animal_index-1][1], animals[animal_index-1][2])

            for i, employee in enumerate(employees):
                print(f"{i+1}. Имя: {employee[1]}, Тип: {employee[2]}")

            employee_index = int(input("Выберите сотрудника-зоолога: "))
            selected_employee = Zookeeper(employees[employee_index-1][1]) if employees[employee_index-1][2] == 'zookeeper' else None

            if selected_employee:
                zoo.perform_action('feed', selected_employee, selected_animal)
            else:
                print("Выбранный сотрудник не является зоологом.")

        elif choice == '4':
            animals = zoo.get_all_animals()
            employees = zoo.get_all_employees()

            if not animals or not employees:
                print("Сначала добавьте хотя бы одного сотрудника и одно животное.")
                continue

            for i, animal in enumerate(animals):
                print(f"{i+1}. Имя: {animal[1]}, Вид: {animal[2]}")

            animal_index = int(input("Выберите животное для лечения: "))
            selected_animal = Animal(animals[animal_index-1][1], animals[animal_index-1][2])

            for i, employee in enumerate(employees):
                print(f"{i+1}. Имя: {employee[1]}, Тип: {employee[2]}")

            employee_index = int(input("Выберите сотрудника-врача: "))
            selected_employee = Veterinarian(employees[employee_index-1][1]) if employees[employee_index-1][2] == 'veterinarian' else None

            if selected_employee:
                zoo.perform_action('treat', selected_employee, selected_animal)
            else:
                print("Выбранный сотрудник не является врачом.")

        elif choice == '5':
            animals = zoo.get_all_animals()
            for i, animal in enumerate(animals):
                print(f"{i+1}. Имя: {animal[1]}, Вид: {animal[2]}")

        elif choice == '6':
            employees = zoo.get_all_employees()
            for i, employee in enumerate(employees):
                print(f"{i+1}. Имя: {employee[1]}, Тип: {employee[2]}")

        elif choice == '7':
            zoo.close_connection()
            print("Соединение с базой данных закрыто.")

        elif choice == '8':
            print("До свидания!")
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == '__main__':
    main()