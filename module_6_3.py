import random

class Animal: # класс описывающий животных
    live = True
    sound = None # звук изначально отсутствует
    _DEGREE_OF_DANGER = 0 # степень опасности животного

    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа, определяется при создании объекта
        # ??? speed = ... ??? - с ellipsis так и не разобрался

    def move(self, dx, dy, dz): # должен менять координаты в _cords на dx, dy и dz, где множителем будет speed.
        # Если при попытке изменения координаты z в _cords значение будет меньше 0,
        # то выводить сообщение "It's too deep, i can't dive :(", и изменения не вносятся.
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self): # выводит координаты: "X, Y, Z>"
        return print('X:', self._cords[0], 'Y:', self._cords[1], 'Z:', self._cords[2])

    def attack(self): # если степень опасности меньше 5: "Sorry, i'm peaceful :)",
        # если больше: "Be careful, i'm attacking you 0_0"
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self): # выводит строку со звуком sound
        return print(self.sound)

class Bird(Animal): # класс описывающий птиц
    beak = True # наличие клюва

    def lay_eggs(self): # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        print("Here are(is)", random.randint(1, 4), "eggs for you")
        # ??? Method 'lay_eggs' may be 'static' ??? - с одной стороны - да, а с другой, он только для птиц

class AquaticAnimal(Animal): # класс описывающий водоплавающих
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # изменение координаты z в _cords
        # Изменяется в отрицательную сторону координату z уменьшенную в 2 раза с учётом скорости
        self._cords[2] = abs(int(self._cords[2] - dz / 2 * self.speed))
        return

class PoisonousAnimal(Animal): # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird): # класс описывающий утконоса
    sound = "Click-click-click" # звук, который издаёт утконос

# Пример работы программы:
db = Duckbill(10) # утконос
print(db.live) # живой
print(db.beak) # с клювом
db.speak() # издаёт звук
db.attack() # атакует
db.move(1, 2, 3) # координаты
db.get_cords() # вывод координат
db.dive_in(6) # изменение координаты по z
db.get_cords() # вывод координат
db.lay_eggs() # количество в кладке яиц