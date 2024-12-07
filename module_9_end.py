def is_prime(func): # функция декоратор, которая распечатывает "Простое", если результат 1ой функции простое число
    # и печатать "Составное" в противном случае
    def wrapper(*args):
        number = func(*args)
        simple = True # создаем флаг(истина)
        for i in range(2, number): # перебираем все делители числа, от 2 до самого числа(не включительно)
            if number % i == 0: # если число делится на делитель без остатка
                simple = False # меняется флаг(ложь)
                print('Составное')
                break # прерываем цикл
        if simple == True: # проверка флага, если истина то печатать 'Простое'
            # ??? при замене False на 0 и True на 1 не выскакивает замечание Expression can be simplified ???
            print('Простое')
        return number
    return wrapper

@is_prime
def sum_three(a, b, c): # функция, которая складывает 3 числа
    return a + b + c

# Пример:
result = sum_three(2, 3, 6)
print(result)