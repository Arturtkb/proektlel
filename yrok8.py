class MyException(Exception):
    def __init__(self, my_date):
        self.date = my_date
    def __str__(self):
        return f"{self.date} Це мій класс"
    


a = int(input())

b = int(input())
try:
    print(a/b)
    print(name)
except ZeroDivisionError:
    print('Помилка. Спроба ділення на 0')
except NameError:
    print("Помилка. Невідоме ім'я")
except:
    print("Помилка.")
print('Кінець програми')