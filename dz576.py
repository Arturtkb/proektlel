class Human:
    height = 180
    age = 40
    work = None
    gladness = 50

class Student(Human):
    age = 18

class Worker(Human):
    height = 185
    gladness = 30
class Programmer(Student):
    work = "Programmer"
    gladness = 60
    def __init__(self):
        print(f"{self.work:=^50}", "\n")
        print(self.gladness)
        print(self.work)
        print(self.age)
        print(self.height)


class Biologist(Student):
    work = "Biologist"
    height = 170
    def __init__(self):
        print(f"{self.work:=^50}", "\n")
        print(self.gladness)
        print(self.work)
        print(self.age)
        print(self.height)

class builder(Worker):
    work = "Builder"
    def __init__(self):
        print(f"{self.work:=^50}", "\n")
        print(self.gladness)
        print(self.work)
        print(self.age)
        print(self.height)



Programmer()
Biologist()
builder()





