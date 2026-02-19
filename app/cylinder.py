import math

class Cylinder:
    """Класс для расчета площади поверхности цилиндра"""
    
    def __init__(self, radius, height):
        """
        Инициализация цилиндра
        :param radius: радиус основания
        :param height: высота цилиндра
        """
        self.radius = radius
        self.height = height
    
    def calculate_surface_area(self):
        """
        Расчет площади полной поверхности цилиндра
        Формула: S = 2πr² + 2πrh = 2πr(r + h)
        """
        return 2 * math.pi * self.radius * (self.radius + self.height)
