import sqlite3

connection = sqlite3.connect("database.sl3", 5)
cur = connection.cursor()
cur.execute("create table users (id int primary key not null, login text, password text);")
cur.execute("insert into user (id, login, password) values (1, 'user1', 'pass1');")
cur.execute("select * from users;")
connection.commit()
res = cur.fetchall()
print(res)
#print(connection)
#print(cur)

connection.close()