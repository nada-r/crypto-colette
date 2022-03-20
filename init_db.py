import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, img) VALUES (?, ?)",
            ('Le Monde', './static/img/1.jpeg')
            )

cur.execute("INSERT INTO posts (title, img) VALUES (?, ?)",
            ('La scene', './static/img/2.jpeg')
            )

cur.execute("INSERT INTO posts (title, img) VALUES (?, ?)",
            ('La nuit', './static/img/3.jpeg')
            )

connection.commit()
connection.close()
