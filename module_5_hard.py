from time import sleep # для отсчета секунд

class User: # пользователи UrTube

    def __init__(self, nickname, password, age):
        self.nickname = nickname # имя пользователя, строка
        self.password = password # пароль в хэшированном виде, число
        self.age = age # возраст, число

    def __repr__(self): # для отображения имя пользователя
          return self.nickname

    def __eq__(self, other): # для сравнения паролей в хэшированном виде
        return self.password == other.password

    def __hash__(self): # для хеширования пароля
        return hash(self.password)


class Video: # видеоролики UrTube

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки (изначально 0)
        self.adult_mode = adult_mode # ограничение по возрасту, bool (False по умолчанию)


class UrTube: # оболочка UrTube

    def __init__(self):
        self.users = [] # список пользователей
        self.videos = [] # список роликов
        self.current_user = None # текущий пользователь

    def log_in(self, nickname, password): # вход в UrTube
        # принимает на вход аргументы: nickname, password и пытается найти пользователя в users
        for user in self.users: # перебираем пользователей в списке пользователей
            if user.nickname == nickname: # если имя совпадает с именем из списка
                if user.password == hash(password): # и если хэшированные пароли совпадают
                    self.current_user = user # пользователь становится текущим пользователем
                    return
        print("Неверный логин или пароль") # иначе печатает

    def register(self, nickname, password, age): # регистрация
        for user in self.users: # перебираем пользователей в списке пользователей
            if user.nickname == nickname: # если имя регистрированного совпадает с именем из списка
                return print(f"Пользователь {nickname} уже существует") # выход из регистрации
        new_user = User(nickname, hash(password), age) # имя, пароль и возраст принимает новый пользователь
        self.current_user = new_user # новый пользователь, вход в UrTube выполняется автоматически
        self.users.append(new_user) # новый пользователь добавляется в список пользователей

    def log_out(self): # для сброса текущего пользователя на None
        self.current_user = None

    def add(self, *added_videos): # принимает неограниченное кол-во объектов класса Video
        for video in added_videos: # перебираем видео в списке видео
            if not any(v.title == video.title for v in self.videos):# если с таким названием видео ещё не существует
                self.videos.append(video)# добавляет в videos

    def get_videos(self, search_word): # принимает поисковое слово и возвращает список названий всех видео,
        # содержащих поисковое слово(не учитывать регистр)
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        # принимает название фильма, если находит, то воспроизводится (ведётся отчёт в консоль)
        video_found = next((video for video in self.videos if video.title == title), None)
        # найденное видео (итерации пока не найдётся видео, в случае исчерпания элементов, возвращает None)
        if self.current_user is None: # если нет пользователя, выход из воспроизведения
            return print('Войдите в аккаунт, чтобы смотреть видео')
        elif video_found is None: # если не найдено видео, выход из воспроизведения
            return
        elif video_found.adult_mode and self.current_user.age < 18:
            # если есть ограничения по возрасту и текущий пользователь младше 18, выход из воспроизведения
            return print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else: # иначе воспроизводится (ведётся отчёт в консоль)
            while video_found.duration > video_found.time_now:
                # цикл пока отсчет времени не достигнет продолжительности видео
                video_found.time_now += 1
                print(video_found.time_now)
                sleep(1)
            print('Конец видео')
            video_found.time_now = 0 # текущее время просмотра данного видео сбрасывается


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')