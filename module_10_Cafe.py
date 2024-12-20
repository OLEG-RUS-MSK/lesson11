from threading import Thread # для управления потоками
from random import randint # для случайного числа
from time import sleep # для отсчёта времени
from queue import Queue # для управления очередью

# Задача "Потоки гостей в кафе": Необходимо имитировать ситуацию с посещением гостями кафе.
class Table: # стол, хранит информацию о находящемся за ним гостем (Guest)

    def __init__(self, number):
        self.number = number # номер стола
        self.guest = None # гость, который сидит за этим столом (по умолчанию None)


class Guest(Thread): # гость, поток, при запуске которого происходит задержка от 3 до 10 секунд

    def __init__(self, name):
        super().__init__() # вызывать метод init родительского класса
        self.name = name # имя гостя

    def run(self): # происходит ожидание случайным образом от 3 до 10 секунд
        sleep(randint(3, 10))


class Cafe: # кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей и их обслуживания

    def __init__(self, *tables: Table):
        self.tables = tables # столы в этом кафе
        self.queue = Queue() # очередь (объект класса Queue)

    def guest_arrival(self, *guests: Guest): # прибытие гостей
        for guest in guests: # перебор гостей из списка гостей
            free_table = None # свободный стол
            for table in self.tables: # перебор столов в кафе
                if table.guest is None: # если есть стол без гостя
                    free_table = table # присвоить столу - свободный стол
                    break
            if free_table: # если есть свободный стол
                free_table.guest = guest # посадить гостя за свободный стол
                guest.start() # запускать поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else: # если же свободных столов для посадки не осталось
                self.queue.put(guest) # помещать гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self): # этот метод имитирует процесс обслуживания гостей
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            # цикл жив пока очередь не пустая (метод empty) или хотя бы один стол занят (not None)
            for table in self.tables: # перебор столов в кафе
                if table.guest is not None: # если стол занят (not None)
                    if not table.guest.is_alive(): # если за столом гость закончил приём пищи(поток завершил работу)
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None # стол освободился
                        if not self.queue.empty() and table.guest is None:
                            # если очередь ещё не пуста (метод empty) и один из столов освободился (None)
                            visitor = self.queue.get() # гость взятый из очереди
                            table.guest = visitor # посадить гостя за свободный стол
                            print(f"{visitor.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                            visitor.start() # запустить поток этого гостя


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()