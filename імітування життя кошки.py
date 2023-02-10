import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness_cat_owner = 30
        self.gladness = 50
        self.hunger = 10
        self.toilet = 0
        self.drowsiness = 0
        self.alive = True

    def to_go_toilet(self):
        print("Пошел в туалет")
        self.toilet -= 6
        self.gladness_cat_owner -= 1


    def to_eat(self):
        print("КУШАТЬ")
        self.hunger += 2


    def to_sleep(self):
        print("кот спит")
        self.gladness -= 5
        self.hunger -= 0.5
        self.drowsiness -= 3

    def to_have_fun(self):
        print("Кот играется")
        self.hunger -= 1
        self.gladness += 6
        self.gladness_cat_owner += 5
        self.drowsiness += 4

    def to_have_tigiduk(self):
        print("Кот решил сделать ТЫГЫДЫК")
        self.hunger -= 0.5
        self.gladness += 10
        self.gladness_cat_owner -= 5
        self.drowsiness += 3



    def is_alive(self):
        if self.gladness_cat_owner < 0:
            print("Барсик надоел и его выгнали")
            self.alive = False
        if self.gladness < 0:
            print("Барсик в кошачей депресии")
            self.alive = False

        if self.hunger < 0:
            print("Барсик умер от голода")
            self.alive = False

    def end_of_day(self):
        print(f'Задоволеність - {self.gladness}')
        print(f'Голод - {self.hunger}')
        print(f'Задоволеність хозяїв - {self.gladness_cat_owner}')

    def live(self, day):
        info = f'День {day}'
        print(f'{info:=^40}')
        if self.gladness_cat_owner <= 10:
            self.to_have_fun()
        elif self.hunger <= 4:
            self.to_eat()
        elif self.gladness <= 30:
            choice1 = random.randint(1, 2)
            if choice1 == 1:
                self.to_have_fun()
            elif choice1 == 2:
                self.to_have_tigiduk()
        elif self.drowsiness >= 7:
            self.to_sleep()
        elif self.toilet >= 10:
            self.to_go_toilet()
        if self.gladness_cat_owner > 10 and self.hunger > 4 and self.gladness > 30 and self.drowsiness < 7 and self.toilet < 10:
            choice = random.randint(1, 4)
            if choice == 1:
                self.to_eat()
            elif choice == 2:
                self.to_sleep()
            elif choice == 3:
                self.to_have_fun()
            elif choice == 4:
                self.to_have_tigiduk()
            self.end_of_day()
            self.is_alive()



barsik = Cat(name="Барсик")
for day in range(365):
    if barsik.alive == False:
        break
    barsik.live(day)