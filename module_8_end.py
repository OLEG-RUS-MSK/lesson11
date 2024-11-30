class Car:

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model # - название автомобиля (строка)
        self.__vin = vin # - vin номер автомобиля (целое число)
        self.__is_valid_vin(vin)
        self.__numbers = numbers # - номера автомобиля (строка)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin): # - принимает vin и проверяет его на корректность
        if not isinstance(vin, int): # выбрасывает исключение, если передано не целое число
            raise IncorrectVinNumber(f'Некорректный тип vin номер')
        if len(str(vin)) != 7: # выбрасывает исключение,
            # если переданное число находится не в диапазоне от 1000000 до 9999999
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        else:
            return True # возвращает True, если корректный

    def __is_valid_numbers(self, numbers): #- принимает numbers и проверяет его на корректность
        if not isinstance(numbers, str): # выбрасывает исключение, если передана не строка
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        if len(numbers) != 6: # выбрасывает исключение, если передана строка не состоит ровно из 6 символов
            raise IncorrectCarNumbers(f'Неверная длина номера')
        else:
            return True # возвращает True, если корректный

class IncorrectVinNumber(Exception): # Класс исключения

    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception): # Класс исключения

    def __init__(self, message):
        self.message = message

# Пример результата выполнения программы:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')