class Student:
    count_of_Student = 0
    def __init__(self, name=None, height=160, IQ=90):
        self.IQ = IQ
        self.name = name
        self.height = height
        Student.count_of_Student += 1
        print("Ку, я  чел")
    def grow(self, height=1):
        self.height += height

    def grow2(self, IQ=1):
        self.IQ += IQ+1.5

    def __str__(self):
        return f'Привет, я чебурек {self.name}, ы  {self.height} ы\n Мой IQ - {self.IQ}'
    def __del__(self):
        print(f'Привіт, я. {self.name} пішов')

student = Student()
print(student.height)

serg = Student(height=180)
print(serg.name)

Artur = Student(name='Artur', height=165, IQ=90)
print(Artur)
print(Artur.height)

