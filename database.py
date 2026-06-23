import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              roll TEXT,
              subject TEXT,
              marks INTEGER)''')

conn.commit()
conn.close()

print("Table banla! students.db ready")