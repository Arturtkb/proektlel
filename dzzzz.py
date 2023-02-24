import colorama
from colorama import init, Fore # импортируем из коламы

colorama.init()
def blue(text):
    print("\033[34m{}".format(text)) #меняет цвет текста на синий
blue("hello world")

def red_fon(text):
    print("\033[41m".format(text)) #меняет цвет фона текста
red_fon("hello world")

print(Fore.WHITE + 'привет') #позволяет писать текст на фоне