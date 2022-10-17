import sqlite3
import os
def create_connection():
    filename = os.path.abspath(__file__)
    dbdir = filename.rstrip('db.py')
    dbpath = os.path.join(dbdir, "pacemaker.db")
    conn = sqlite3.connect(dbpath)
    return conn

def create_database(conn):
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username text NOT NULL,
        password text NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT
    )""")
    conn.commit()

def insert_users(conn, username, password):
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username,password))
    conn.commit()

def list_users(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    return c.fetchall()

def main():
    conn = create_connection()
    create_database(conn)
    insert_users(conn, 'Test', 'Test') 
    print(list_users(conn))
    conn.close()

main()
