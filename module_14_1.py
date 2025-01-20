import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i + 1}", f"example{i + 1}@gmail.com", i * 10 + 10, "1000"))

# for i in range(1, 11):
#     if i % 2:
#         cursor.execute("UPDATE Users set balance = balance - 500 WHERE id = ?", (f"{i}"))

# for i in range(1, 11):
#     j = i + 2
#     if not j % 3:
#         cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    if user[3] != 60:
        print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")


connection.commit()
connection.close()