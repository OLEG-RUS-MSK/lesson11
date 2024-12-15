import threading # для управления потоками
from random import randint # для случайного числа
from time import sleep # для отсчёта времени

# Задача "Банковские операции"
class Bank:

    def __init__(self):
        self.balance: int = 0 # баланс банка (int)
        self.lock = threading.Lock() # объект класса Lock для блокировки потоков

    def deposit(self): # пополнения средств
        for i in range(100):
            profit = randint(50, 500) # случайное целое число от 50 до 500
            self.balance += profit # пополнения баланса на случайное целое число
            if self.balance >= 500 and self.lock.locked(): # если баланс больше или равен 500 и замок lock заблокирован
                self.lock.release() # разблокировать его методом release
            print(f'Пополнение: {profit}. Баланс: {self.balance}')
            sleep(.001) # ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения


    def take(self): # снятие средств
        for i in range(100):
            gone = randint(50, 500) # случайное целое число от 50 до 500
            print(f'Запрос на {gone}')
            if gone <= self.balance: # если случайное число меньше или равно текущему балансу
                self.balance -= gone # производится снятие, на соответствующее число
                print(f'Снятие: {gone}. Баланс: {self.balance}')
            else: # если случайное число оказалось больше баланса
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire() # заблокировать поток методом acquire
            sleep(.001) # нет в задании, но решил поставить ожидание


bk = Bank() # создание объекта класса Bank

th1 = threading.Thread(target=Bank.deposit, args=(bk,)) # создание потока-1 для его метода deposit
th2 = threading.Thread(target=Bank.take, args=(bk,)) # создание потока-2 для его метода take

th1.start() # запуск потока
th2.start()
th1.join() # для синхронизации потоков
th2.join()

print(f'Итоговый баланс: {bk.balance}')