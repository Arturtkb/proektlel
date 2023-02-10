import random

class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name =name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self.glasdness = 50
        self.satiete = 50

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, purchase):
        pass

    def cleaning(self):
        pass

    def to_repair(self):
        pass

    def chll(self):
        pass


    def get_house(self):
        self.house = House()

    def get_car(self):
        self.car = Car(brand_of_cars)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_lst)


    def is_alive(self):
        if self.glasdness < 0:
            print("Депресия 1000-7")
            return False
        if self.satiete < 0:
            print("УМЕР ОТ ГОЛОДА УЖС")
            return False
        if self.money < -200:
            print("бомж")
            return False


    def day_info(self, day_number):
        day_str = f"День {day_number}-й з життя {self.name}-а"
        print(f"{day_str:=^50}", "\n")
        human_str = f"ИНФА ПРО{self.name}а"
        print(f"{human_str:=^50}", "\n")
        print(f"Задоволеність{self.glasdness}")
        print(f"Ситість{self.satiete}")
        print(f"ДЕНЬГИ{self.money}")
        house_str = f"ИНФА ПРО дом"
        print(f"{house_str:=^50}", "\n")
        print(f"ІЖА - {self.house.food}")
        print(f"Порядок{self.house.mess}")
        car_str = f"ИНФА ПРО АВТІВКУ {self.name}а"
        print(f"{car_str:=^50}", "\n")
        print(f"Пальне - {self.car.fuel}")
        print(f"Стан - {self.car.strength}")


    def live(self, day_number):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
            print("поселитися в будинку")
        if self.car is None:
            self.get_car()
            print(f"Придбав автівку {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"ВЛАШТУВАВСЯ НА РОБОТУ {self.job.job}{self.job.salary}")
        self.day_info(day_number)
        if self.money < 0:
            print("ЕКАРНЫЙ БАБАЙ НАДО ЧТО-ТО ДЕЛАТЬ")




brand_of_cars = {"BMV" : {"fuel": 100, "strength": 100, "consumption": 6},
                 "Audi" : {"fuel": 80, "strength": 80, "consumption": 7},
                 "MErcedes" : {"fuel": 100, "strength": 90, "consumption": 5},
                 "Запорожець" : {"fuel": 50, "strength": 50, "consumption": 8}}


class Car:
    def __init__(self, brand_of_cars):

        self.brand = random.choice(list(brand_of_cars))
        self.fuel = brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strength"]
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("немає пального або авто зломалося")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


job_lst = {"Разработчик пайтон" : {"salary": 100, "gladness_less": 10},
           "ЮТУБЕР ЮХУ" : {"salary": 60, "gladness_less": 2},
           "Продавец" : {"salary": 50, "gladness_less": 8},
           "Парихмахер" : {"salary": 50, "gladness_less": 5}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


anton = Human("Антон")
for day in range(1, 366):
    if anton.live(day) == False:
        break
