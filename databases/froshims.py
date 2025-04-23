import sqlite3

# Create/connect to database
conn = sqlite3.connect('froshims.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE registrants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sport TEXT NOT NULL
)
''')

# Commit changes and close connection
conn.commit()
conn.close()