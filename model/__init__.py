import sqlite3

conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

query_create = 'CREATE TABLE IF NOT EXISTS tasks (data INTEGER, task TEXT, status TEXT)'
cur.execute(query_create)


conn.close()