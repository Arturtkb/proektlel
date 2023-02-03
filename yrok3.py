import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True


    def to_study(self):
        print("Я учится")
        self.progress += 0.1
        self.gladness -= 5


    def to_sleep(self):
        print("я спать")
        self.gladness += 3

    def to_have_fun(self):
        print("я играю в кс не мешай")
        self.progress -= 0.1
        self.gladness += 6

    def is_alive(self):
        if self.progress < 0:
            print("Вы исключенны из школы")
            self.alive = False
        if self.progress > 5:
            print("Ура я завершил школу быстреееееее")
            self.alive = False
        if self.gladness < 0:
            print("я умер прости 1000-7")
            self.alive = False

    def end_of_day(self):
        print(f'Задоволеність - {self.gladness}')
        print(f'Прогрес - {self.progress}')

    def live(self, day):
        info = f'День {day} з життя {self.name}'
        print(f'{info:=^40}')
        choice = random.randint(1, 3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_have_fun()
        self.end_of_day()
        self.is_alive()


leonid = Student(name="Леонід")
for day in range(365):
    if leonid.alive == False:
        break
    leonid.live(day)
