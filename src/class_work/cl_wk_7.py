import sqlite3

conn = sqlite3.connect('member.db')
c = conn.cursor()

def create_table():
    c.execute('''create table if not exists member (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    )''')
conn.commit()