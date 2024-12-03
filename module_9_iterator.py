class StepValueError(ValueError): # класс исключения, который наследуется от ValueError
    pass

class Iterator: # класс итерации

    def __init__(self, start: int, stop: int, step=1):
        if step == 0: #  проверяется, если шаг равен нулю, то выбрасывается исключение
            raise StepValueError ('шаг не может быть равен 0')
        self.start = start # целое число, с которого начинается итерация
        self.stop = stop # целое число, на котором заканчивается итерация
        self.step = step # шаг, с которым совершается итерация
        self.pointer = start # указывает на текущее число в итерации (изначально start)

    def __iter__(self): #  - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора
        self.pointer = self.start
        return self

    def __next__(self): # метод, увеличивающий атрибут pointer на step
        if self.step > 0 and self.pointer > self.stop: # если шаг положительный
            raise StopIteration
        if self.step < 0 and self.pointer < self.stop: # если шаг отрицательный
            raise StopIteration
        range_list = self.pointer
        self.pointer += self.step
        return range_list


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()