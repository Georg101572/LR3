class ElementИванов:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

my_element = ElementЯшкин("Азот", "N", 7)

# Выводим информацию
print("Создан элемент:")
print(f"Название: {my_element.name}")
print(f"Символ: {my_element.symbol}")
print(f"Номер: {my_element.number}")
