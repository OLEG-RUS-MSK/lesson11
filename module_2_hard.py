# import random
# def first_stone():
#     rand_ = [i for i in range(3, 21)]
#     stone_1 = random.choice(rand_)
#     return stone_1
#
# print("первый камень: ", first_stone())
# если снять коментарии, то программа сама сгенирирует случайное число(эту строчку надо будет удалить)

dict_ = {}
for a in range(3, 21): # цикл для создания словаря
    mean = []  # временный списпок для значений ключа
    for b in range(1, a): # цикл для кратности
        sum_ = a / (a - b)
        if a % (a - b) != 0:
            continue
        else: # если кратно
            for a1 in range(1, int(sum_)): # цикл для суммы
                a2 = sum_ - a1
                if a2 > a1:
                    mean.append([a1, int(a2)])
                else:
                    break
    mean.sort()
    result = [] # временный список для сортированных пар и объединения в одно число
    for x in mean:
        result.extend(x) # последовательное добавление чисел из списка для значения ключа
    dict_.update({a: ''.join(map(str, result))})

n = int(input("Введите число от 3 до 20: ", ))
while n < 3 or n > 20:
    n = int(input("Неправильное число, введите ещё раз число от 3 до 20: ", ))

print('Результат: ', dict_[n])