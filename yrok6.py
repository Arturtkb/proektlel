class Human:
    height = 170
    age = 30
    gladness = 50

class Student(Human):
    pass

class Aspirant(Student):
    height = 180
    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.gladness)
    def _hello(self):
        print("_ПРИВЕТ")

    def __hello(self):
        print("__ПРИВЕТ")



class Worker(Human):
    age = 50

class Hello_Kity:
    hello = "А"
    _hello = "АА"
    __hello = "ААА"

    def __init__(self):
        self.kity = "китти"
        self._kity = "_китти"
        self.__kity = "__китти"

    def __method(self):
        print("Method")


class Hi(Hello_Kity):
    def print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)

class Computer:
    def __init__(self):
        super().__init__()
        self.RAM = "16 gb"
        self.model = ""
    def calc(self):
        print("Calculate")

class Monitor:
    def __init__(self, model, ):
        super().__init__()
        self.resolution = "8K"
    def display(self):
        print("print resuly")

class SmartPhone(Computer, Monitor):
    def info(self):
        print(self.resolution)
        print(self.RAM)
        print(self.model)


phone = SmartPhone(model="Apple 15")
phone.info()




hello = Hello_Kity()
hello.print()

hi = Hi()
hi.hi_print()

asp = Aspirant()
asp.age = 10000

