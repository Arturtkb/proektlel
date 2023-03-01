import sqlite3




connection = sqlite3.connect("basa.sl3", 2)
cur = connection.cursor()
#cur.execute("create table users (login, password);")


pochatok = float(input("Щоб ви хотіли зробити? 1) Зареєстурватися, 2) Війти"))
if pochatok == 1:
    login1 = str(input("Введіть логін"))
    password1 = str(input("Введіть пароль"))
    cur.execute(f"insert into users (login, password) values ('{login1}', '{password1}');")
    cur.execute("select login, password from users")
    connection.commit()
    print("Ви зареєструвалися")
    print("Войдите:")
    log = str(cur.fetchall())
    print(log)
    login2 = str(input("Введіть ваш логін"))
    password2 = str(input("Введіть ваш пароль"))
    loginxpass = (login2, password2)
    print(loginxpass)
    if loginxpass == str(log):
        print("Вхід успішний")
    else:
        print("вхід не вдався")


else:
    log = str(cur.fetchall())
    print(log)
    login2 = str(input("Введіть ваш логін"))
    password2 = str(input("Введіть ваш пароль"))
    loginxpass = str([(login2, password2)])
    print(loginxpass)
    if loginxpass == str(log):
        print("Вхід успішний")
    else:
        print("вхід не вдався")

connection.close()


