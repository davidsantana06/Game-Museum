import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash


# DATABASE CONNECTION -------------------------------
print("Connecting to MySQL")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('User or Password wrongs')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `game_museum`;")

cursor.execute("CREATE DATABASE `game_museum`;")

cursor.execute("USE `game_museum`;")
# ---------------------------------------------------


# TABLES -------------------------------------------------------
TABLES = {}
TABLES['Games'] = ('''
      CREATE TABLE `games` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `plataform` varchar(30) NOT NULL,
      `mushrooms` int(1) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `username` varchar(12) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`username`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
    table_sql = TABLES[table_name]
    try:
        print('Creating {} table:'.format(table_name), end=' ')
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Already exists')
        else:
            print(err.msg)
    else:
        print('OK')
# --------------------------------------------------------------


# INSERTING USERS --------------------------------------------------
users_sql = 'INSERT INTO users (username, password) VALUES (%s, %s)'
users = [
    ('admin', generate_password_hash('admin').decode("utf-8"))]
cursor.executemany(users_sql, users)

cursor.execute('select * from game_museum.users')
print('\n_Users:')
for user in cursor.fetchall():
    print(user[0])
# ------------------------------------------------------------------

# INSERTING GAMES --------------------------------------------------------------
games_sql = 'INSERT INTO games (name, plataform, mushrooms) VALUES (%s, %s, %s)'
games = [
    ('The Witcher 3: Wild Hunt', 'PC', '5'),
    ('God of War: Ragnarok', 'PS5', '5'),
    ('Dark Souls III', 'PS4', '4'),
    ('Sekiro: Shadows Die Twice', 'PS4', '5')
]
cursor.executemany(games_sql, games)

cursor.execute('select * from game_museum.games')
print('\n_Games:')
for game in cursor.fetchall():
    print(game[1])
# ------------------------------------------------------------------------------

# COMMIT -----
conn.commit()

cursor.close()
conn.close()
# ------------
