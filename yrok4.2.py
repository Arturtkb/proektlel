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

brand_of_cars = {"BMV" : {"fuel": 100, "strength": 100, "consumption": 6},
                 "Audi" : {"fuel": 80, "strength": 80, "consumption": 7},
                 "MErcedes" : {"fuel": 100, "strength": 90, "consumption": 5},
                 "Запорожець" : {"fuel": 50, "strength": 50, "consumption": 8}}


class Car:
    def __init__(self, brand_of_cars):

        self.brand = random.choice(list(brand_of_cars))
        self.fuel = brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strenght"]
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        pass

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


job_lst = {"Разработчик пайтон" : {"salary": 100, "gladness_less": 10},
           "ЮТУБЕР ЮХУ" : {"salary": 60, "gladness_less": 2},
           "Продавец" : {"salary": 50, "gladness_less": 8},
           "Парихмахер" : {"salary": 50, "gladness_less": 5}}


class job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


