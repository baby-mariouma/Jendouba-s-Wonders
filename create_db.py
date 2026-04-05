import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    
    place TEXT,
    review TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")