import math
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cylinder import Cylinder

def test_cylinder():
    """Функция для тестирования класса Cylinder"""
    
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ КЛАССА CYLINDER")
    print("=" * 50)
    
    # Тестовые данные
    test_cases = [
        (1, 1),    # радиус 1, высота 1
        (2, 3),    # радиус 2, высота 3
        (5, 10),   # радиус 5, высота 10
        (0.5, 2),  # радиус 0.5, высота 2
    ]
    
    for i, (radius, height) in enumerate(test_cases, 1):
        cylinder = Cylinder(radius, height)
        area = cylinder.calculate_surface_area()
        
        # Ручной расчет для проверки
        expected = 2 * math.pi * radius * (radius + height)
        
        print(f"\nТест {i}:")
        print(f"  Радиус: {radius}, Высота: {height}")
        print(f"  Результат: {area:.4f}")
        print(f"  Ожидалось: {expected:.4f}")
        
        # Проверка с погрешностью
        if abs(area - expected) < 0.0001:
            print("  ✅ ТЕСТ ПРОЙДЕН")
        else:
            print("  ❌ ТЕСТ НЕ ПРОЙДЕН")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    test_cylinder()
