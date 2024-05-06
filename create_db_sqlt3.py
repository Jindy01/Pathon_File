import sqlite3

# conn = sqlite3.connect('example.db')
# cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS employees (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 age INTEGER NOT NULL)''')

# cur.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('John Doe', 30))
# cur.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Alice Smith', 25))

# conn.commit()


# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# cur.execute("DROP TABLE IF EXISTS employees")

# for row in rows:
#     print(row)

# conn.commit()
# conn.close()


# Туториал !

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

is_create_new_user = int(input('Если создать напишите: '))
username, create_new_email, create_new_age = None, '', 0

def create_new_user():
    create_new_username = str(input('Write new user name: '))
    create_new_email = str(input('Write new user imail: '))
    create_new_age = int(input('Write new user age: '))
    return create_new_username, create_new_email, create_new_age

if is_create_new_user == 1:
    username, create_new_email, create_new_age = create_new_user()


# Создаёт индекс для столбца " email "
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# Создаёт нового пользователя а так же блокирует создание дубликата 
cursor.execute('INSERT OR IGNORE INTO Users (username, email, age) VALUES (?, ?, ?)', (username, create_new_email, create_new_age))
# Обновляет данные пользователя " newuser "
# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))
# Удаляет пользователя по имени " newuser "
# cursor.execute('DELETE FROM Users WHERE username = ?', ('1', ))
# Извлекает данные из таблицы " Users "
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# [print(user) for user in users]
# Выбирает имина и возвраст пользователей старше 25 лет
# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
# result = cursor.fetchall()
# [print(row) for row in result]
# Получаем средний вощвраст пользователей для каждого возраста
# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
# result_for_age = cursor.fetchall()
# [print(row) for row in result_for_age]
# Фильтруем группы по среднему возрасту больше 30 
# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30, ))
# filtered_results = cursor.fetchall()
# [print(row) for row in filtered_results]
# Выбираем и сортируем пользователей по возрасту и убыванию
# cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
# result_min = cursor.fetchall()
# [print(row) for row in result_min]


# connection.commit()
# connection.close()

print(new)