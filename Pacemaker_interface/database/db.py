import sqlite3
import os
def create_connection():
    filename = os.path.abspath(__file__)
    dbdir = filename.rstrip('db.py')
    dbpath = os.path.join(dbdir, "pacemaker.db")
    conn = sqlite3.connect(dbpath)
    return conn

def create_database():
    conn = create_connection()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username text NOT NULL,
        password text NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT
    )""")
    conn.commit()
    conn.close()

def insert_users(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username,password))
    conn.commit()
    conn.close()

def list_users():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    results = c.fetchall()
    conn.close()
    return results

def main():
    create_database()
    print(list_users())

main()
