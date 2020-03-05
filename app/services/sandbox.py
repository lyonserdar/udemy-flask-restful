import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "jose", "testpass")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, "jack", "testpass"),
    (3, "james", "testpass"),
    (4, "daniel", "testpass"),
    (5, "dave", "testpass"),
    (6, "joe", "testpass"),
]
cursor.executemany(insert_query, users)


connection.commit()

connection.close()
