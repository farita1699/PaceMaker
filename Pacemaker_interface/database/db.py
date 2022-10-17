import sqlite3

conn = sqlite3.connect('pacemaker.db')
c = conn.cursor()

def create_database():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS users(
            username text NOT NULL,
            password text NOT NULL,
            id integer PRIMARY KEY AUTOINCREMENT
        )""")

def insert_users():
    with conn:
        c.execute("INSERT INTO users (username, password) VALUES ('Jerry', 'Jerry')")

def list_users():
    with conn:
        c.execute("SELECT * FROM users")
        return c.fetchall()
        
print(list_users())

conn.close()

def create_connection():
    conn = None
    database = r''
    return conn