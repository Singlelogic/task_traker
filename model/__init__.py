import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

query_create = 'CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, date TEXT, task TEXT, done TEXT)'
cur.execute(query_create)

conn.close()