# Задание "Свой YouTube":

from time import sleep
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(stored_password, provided_password):
    return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()


class User:
    users = []

    def __init__(self, nickname: str, password: hash, age: int):
        self.nickname = nickname  # имя пользователя
        self.password = hash_password(password)  # password(в хэшированном виде)
        self.age = age  # возраст


class Video:
    videos = []

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now  # секунда остановки(изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту


class UrTube(User, Video):

    def __init__(self, current_user: str = 'User'):
        self.users = []  # список объектов User
        self.users_ = []  # просто список пользователей
        self.current_user = current_user  # текущий пользователь
        self.video_title = []  # Название видеоролика
        self.current_user_age = int(0)  # Актуальный пользователь
        self.duration = int(0)  # Продолжительность ролика

    def register(self, nickname, password, age):
        for i in range(len(self.users)):
            if (getattr(self.users[i], 'nickname') == nickname and getattr(self.users[i], 'password') !=
                    hash_password(password)):
                print(f'Пользователь {nickname} уже существует. Пароль введён не верно!')
                return
        if len(self.users) == 0 or nickname not in self.users_:
            self.users.append(User(nickname, password, age))
            self.users_.append(nickname)
        UrTube.log_in(self, nickname, password)
        # print('Список пользователей:')
        # print(f'{nickname=}, {password=}, {age=} , {self.users} , {self.users_}')
        # for i in range(len(self.users)):
        #     print(getattr(self.users[i], 'nickname'))
        return

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if (getattr(self.users[i], 'nickname') == nickname and getattr(self.users[i], 'password') ==
                    hash_password(password)):
                self.current_user = nickname
                self.current_user_age = getattr(self.users[i], 'age')
        return

    def log_out(self):  # для сброса текущего пользователя на None
        self.current_user = None

    def add(self, *args):
        video_title = []
        for arg in args:
            if len(self.videos) == 0:
                self.videos.append(arg)
                video_title.append(getattr(arg, 'title'))
                continue
            if getattr(arg, 'title') in video_title:
                continue
            else:
                self.videos.append(arg)
                video_title.append(getattr(arg, 'title'))

        self.video_title = video_title

        print('Список видео:')
        for i in range(len(self.videos)):
            print(getattr(self.videos[i], 'title'))

    def get_videos(self, word):
        video_title = []
        for list_ in self.video_title:
            if word.lower() in list_.lower():
                video_title.append(list_)
        print(f'Слово: "{word}" содержится в названиях следующих файлов:')
        return video_title

    def watch_video(self, name_film: str):
        print(f'Выбран фильм: {name_film}')
        print("")
        if self.current_user == None or self.current_user == 'User':
            print('Войдите в аккаунт, чтобы смотреть видео!')
            print()
            return
        for i in range(len(self.videos)):
            time_now = int(getattr(self.videos[i], 'time_now'))
            adult_mode = bool(getattr(self.videos[i], 'adult_mode'))
            duration = getattr(self.videos[i], 'duration')
            if adult_mode == True:
                adult_mode_ = '18+'
            else:
                adult_mode_ = '6+'
            if name_film == str(getattr(self.videos[i], 'title')):
                self.duration = duration
                print(f'Такое название есть на канале "Свой YouTube", секунда остановки: {time_now}, '
                      f'Продолжительность фильма: {duration} c., {adult_mode_}')
                print(f"Пользователь: {self.current_user}")
                if adult_mode == False:
                    UrTube.playback(self)
                else:
                    if self.current_user_age >= 18:
                        # print(f"Пользователь {self.current_user}, Вам уже есть 18 лет!")
                        UrTube.playback(self)
                    else:
                        print(f"Пользователь {self.current_user}, Вам нет 18 лет, пожалуйста покиньте страницу!")
                        print()
                return
        print(f'Такого фильма: {name_film} на ресурсе "Свой YouTube не существует!')
        UrTube.log_out(self)

    def playback(self):
        print()
        print(f'Ведётся отчёт в консоль на какой секунде ведётся просмотр:')
        for time_now in range(self.duration):
            print(time_now, end=' ')
            sleep(0.5)
        print()
        print('"Конец видео"')
        UrTube.log_out(self)
        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 9, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v4 = Video('Для чего девушкам парень', 10, adult_mode=True)
v5 = Video('Лучший язык программирования 2024 года', 5)
v6 = Video('Лучший язык программирования 2025 года', 8)

# Добавление видео
ur.add(v1, v2, v3, v4, v5, v6)

# Проверка поиска
print()
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print()

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)      # По условиям задания: после просмотра видео пользователь обнуляется.

# Попытка воспроизведения несуществующего видео
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  #
ur.watch_video('Лучший язык программирования 2024 года!')

# Ещё проверки на вход пользователя и возрастное ограничение
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Лучший язык программирования 2025 года')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Лучший язык программирования 2024 года')