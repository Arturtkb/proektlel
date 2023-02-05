import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True
        self.money = 100


    def to_study(self):
        print("Я учится")
        self.progress += 0.1
        self.gladness -= 5
        self.money -= 5


    def to_sleep(self):
        print("я спать")
        self.gladness += 3


    def to_work(self):
        print("я работать")
        self.money += 10

    def to_have_fun(self):
        print("я играю в кс не мешай")
        self.progress -= 0.1
        self.gladness += 6
        self.money -= 15

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
        print(f'Деньги - {self.money}')

    def live(self, day):
        info = f'День {day} з життя {self.name}'
        print(f'{info:=^40}')
        if self.progress < 0.5:
            self.to_study()
        elif self.gladness < 20:
            choice = random.randint(1, 2)
            if choice == 1:
                self.to_sleep()
            if choice == 2:
                self.to_have_fun()
        elif self.money < 40:
            self.to_work()

        if self.money >= 40 and self.progress >= 0.5 and self.gladness >= 20:
            slychainost = random.randint(1, 4)
            if slychainost == 1:
                self.to_study()
            if slychainost == 2:
                self.to_sleep()
            if slychainost == 3:
                self.to_work()
            if slychainost == 4:
                self.to_have_fun()
        self.end_of_day()
        self.is_alive()


leonid = Student(name="Леонід")
for day in range(365):
    if leonid.alive == False:
        break
    leonid.live(day)
