class ElementЯшкин:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
    def dump(self):
        """Метод для вывода всех атрибутов"""
        print("=" * 30)
        print("ИНФОРМАЦИЯ ОБ ЭЛЕМЕНТЕ")
        print("=" * 30)
        print(f"Название: {self.name}")
        print(f"Символ:   {self.symbol}")
        print(f"Номер:    {self.number}")
        print("=" * 30)

my_element = ElementЯшкин("Азот", "N", 7)

# Используем метод dump()
my_element.dump()
