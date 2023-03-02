import sqlite3




connection = sqlite3.connect("bas.sl3", 2)
cur = connection.cursor()
#cur.execute("create table users (name);")
name1 = str(input("Введіть 1 ім'я"))
name2 = str(input("Введіть 2 ім'я"))
name3 = str(input("Введіть 3 ім'я"))
name4 = str(input("Введіть 4 ім'я"))
name5 = str(input("Введіть 5 ім'я"))
cur.execute(f"insert into users (name) values ('{name1}');")
cur.execute("select name from users")
cur.execute(f"insert into users (name) values ('{name2}');")
cur.execute("select name from users")
cur.execute(f"insert into users (name) values ('{name3}');")
cur.execute("select name from users")
cur.execute(f"insert into users (name) values ('{name4}');")
cur.execute("select name from users")
cur.execute(f"insert into users (name) values ('{name5}');")
cur.execute("select name from users")
connection.commit()

nam = str(cur.fetchall())

print(nam)

namevoiti = str(input("проверка имени"))
if namevoiti == nam:
    print("ім'я є в базі")
else:
    print("ім'я не має в базі")