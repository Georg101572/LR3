import sys
import os
import math

# Добавляем путь для импорта модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cylinder import Cylinder

def get_positive_number(prompt):
    """Запрашивает положительное число"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть положительным!")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    """Главная функция программы"""
    print("=" * 50)
    print("ПРОГРАММА РАСЧЕТА ПЛОЩАДИ ПОВЕРХНОСТИ ЦИЛИНДРА")
    print("=" * 50)
    
    # Ввод данных
    print("\nВведите параметры цилиндра:")
    radius = get_positive_number("Радиус основания (см): ")
    height = get_positive_number("Высота цилиндра (см): ")
    
    # Создание объекта и расчет
    cylinder = Cylinder(radius, height)
    area = cylinder.calculate_surface_area()
    
    # Вывод результата
    print("\n" + "-" * 30)
    print("РЕЗУЛЬТАТ РАСЧЕТА:")
    print("-" * 30)
    print(f"Радиус: {radius:.2f} см")
    print(f"Высота: {height:.2f} см")
    print(f"Площадь поверхности: {area:.2f} кв.см")
    print("-" * 30)

if __name__ == "__main__":
    main()
