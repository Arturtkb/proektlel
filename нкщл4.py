class Human:
    def __init__(self, name='No name'):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, *humans):
        for passenger in humans:
            self.passenger.append(passenger)


    def print_passenger(self):
        if self.passenger == []:
            print('Автівка порожня')
        else:
            print(f'Зараз кудись їдуть на {self.brand}')
            for passenger in self.passenger:
                print(passenger.name)

human1 = Human("Сергей")
human2 = Human("Лол")
car = Car("BMW")
car.print_passenger()
car.add_passenger(human1, human2)

car.print_passenger()