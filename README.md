
# Лабораторная работа №3
## Объектно-ориентированное программирование
*Студент: Яшкин Г.А. ПИ-430Б*
*Вариант: 7*
*Элемент: Азот (N, №7)*

### 1. Создание репозитория
Действие	Результат
Создан репозиторий	LR3 на GitHub
Ветка по умолчанию	master
.gitignore	Python
Лицензия	MIT
README.md	Создан
### 2. Реализация класса ElementЯшкин
Файл: ElementЯшкин/element.py

#### 2.1. Базовая структура класса
python
class ElementЯшкин:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
        
#### 2.2. Добавление метода dump()
python
def dump(self):
    print(f"Название: {self.name}")
    print(f"Символ: {self.symbol}")
    print(f"Номер: {self.number}")
    
#### 2.3. Инкапсуляция и геттеры
python
class ElementЯшкин:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number
    
    def dump(self):
        print(f"Название: {self.__name}")
        print(f"Символ: {self.__symbol}")
        print(f"Номер: {self.__number}")
        
#### 2.4. Создание объекта
python
element = ElementЯшкин("Азот", "N", 7)
element.dump()
### 3. Программа расчета площади цилиндра
Структура приложения (папка app/):

text
app/
├── __init__.py
├── cylinder.py
├── main.py
└── test.py

#### 3.1. Класс Cylinder (cylinder.py)
python
import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def calculate_surface_area(self):
        # S = 2πr² + 2πrh = 2πr(r + h)
        return 2 * math.pi * self.radius * (self.radius + self.height)
        
#### 3.2. Основная программа (main.py)
python
from cylinder import Cylinder

def main():
    r = float(input("Радиус: "))
    h = float(input("Высота: "))
    
    c = Cylinder(r, h)
    area = c.calculate_surface_area()
    
    print(f"Площадь: {area:.2f}")

if __name__ == "__main__":
    main()
    
#### 3.3. Тестирование (test.py)
python
from cylinder import Cylinder

def test():
    test_data = [(1, 1), (2, 3), (5, 10)]
    for r, h in test_data:
        c = Cylinder(r, h)
        print(f"r={r}, h={h} -> {c.calculate_surface_area():.2f}")

test()
### 4. Работа с ветками Git
Ветка	Назначение	Статус
feature/cylinder-class	Создание класса Cylinder	Слита
feature/user-interface	Пользовательский интерфейс	Слита
feature/testing	Модуль тестирования	Слита
Для каждой ветки создан Pull Request с последующим слиянием в master.

### 5. Результаты
Созданные классы:
Класс	Атрибуты	Методы
ElementЯшкин	__name, __symbol, __number	dump(), геттеры
Cylinder	radius, height	calculate_surface_area()
Созданный объект:
Элемент: Азот

Символ: N

Номер: 7

### 6. Пример работы программы
text
Введите радиус: 5
Введите высоту: 10
Площадь поверхности: 471.24 кв.см

### 7. Вывод
В ходе работы:

Создан класс Element[Фамилия] с инкапсуляцией данных

Реализован метод dump() для вывода информации

Использованы свойства-геттеры для доступа к приватным атрибутам

Разработана программа расчета площади цилиндра

Освоена работа с ветками и Pull Request'ами в GitHub
