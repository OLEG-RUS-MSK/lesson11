grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
dictionary = {}
for n in range(len(grades)):
    m = sum(grades[n]) / len(grades[n])
    dictionary.update({students_list[n]: m})

print(dictionary)