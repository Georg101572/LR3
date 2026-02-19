class ElementЯшкин:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
        
  # Свойства-геттеры для доступа к приватным атрибутам
    @property
    def name(self):
        """Геттер для name"""
        return self.__name
    
    @property
    def symbol(self):
        """Геттер для symbol"""
        return self.__symbol
    
    @property
    def number(self):
        """Геттер для number"""
        return self.__number
    
    
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

# Демонстрация работы геттеров
print("\nДоступ через геттеры:")
print(f"name: {my_element.name}")
print(f"symbol: {my_element.symbol}")
print(f"number: {my_element.number}")
