import time
from time import sleep
from pprint import pprint

class Users:
    """Авторизация"""

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    """Параметры видео"""
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube(Users):
    """Создание платформы и ее опций"""

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        user = Users(nickname, password, age)
        for us in self.users:
            if us.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        self.users.append(user)
        self.current_user = user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
            else:
                self.log_out()


    def log_out(self):
        self.current_user = None

    def add(self, *video):
         for v in video:
            if v.title  not in self.videos:
                self.videos.append(v)
            else:
                ...

    def get_videos(self, search_word):
        list = []
        for v in self.videos:
            if search_word in v.title or search_word in v.title.lower() or search_word in v.title.upper():
                list.append(v.title)
        return list

    def watch_video(self, name_video):
        if self.current_user is None:
            return print("Войдите в аккаунт, чтобы смотреть видео.")
        else:
            ...
        if self.current_user.age < 18:
            return print('Вам нет 18, пожалуйста покиньте страницу.')
        count = 0
        for v in self.videos:
            if v.title == name_video:
                while count != v.duration:
                    count += 1
                    print(count, end=' ')
                    time.sleep(1)
                count = 0
                print('The End')
            else:
                ...


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin','lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')




"""Осталось малое - довести до идеала регистрацию, нужно чтобы оьращение было к объектам. Второе, нужно чтобы функция
 проверяла возраст и ставила ТРУ, если пользователю больше 18 лет, а там поймешь """