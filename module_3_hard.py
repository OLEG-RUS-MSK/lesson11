data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

lists = []
def calculate_structure_sum(myst):
    for i in myst:
        if isinstance(i, (list, tuple, set)):
            calculate_structure_sum(i)
            continue
        if isinstance(i, dict):
            lists.append(sum(map(int, i.values())) + sum(map(len, i.keys())))
            continue
        if isinstance(i, str):
            lists.append(len(i))
        else:
            lists.append(i)
    return sum(lists)

result = calculate_structure_sum(data_structure)
print(result)

# Я сохранил комментарии для себя, чтобы быстрее разобраться в них в будущем.
# цикл перебирает элементы списка:
# если элемент СПИСОК, КОРТЕЖ или МНОЖЕСТВО, то запускается рекурсия(проверяется есть ли внутри СПИСОК, КОРТЕЖ или МНОЖЕСТВО, и так пока не останется других вариантов)
# если СЛОВАРЬ, то высчитывается сумма ключей и длина значений и добавляется в доп.список
# если СЛОВО, то высчитывается длина слова и добавляется в доп.список
# иначе ЧИСЛО и добавляется в доп.список