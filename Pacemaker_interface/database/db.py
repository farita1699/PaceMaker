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
    c.execute("""CREATE TABLE IF NOT EXISTS AOO(
        LRL integer NOT NULL,
        URL integer NOT NULL,
        APW DOUBLE NOT NULL,
        AA DOUBLE NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS VOO(
        LRL integer NOT NULL,
        URL integer NOT NULL,
        VPW DOUBLE NOT NULL,
        VA DOUBLE NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS AAI(
        LRL integer NOT NULL,
        URL integer NOT NULL,
        APW DOUBLE NOT NULL,
        AA DOUBLE NOT NULL,
        AT DOUBLE NOT NULL,
        RP integer NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS VVI(
        LRL integer NOT NULL,
        URL integer NOT NULL,
        VPW integer NOT NULL,
        VA integer NOT NULL,
        VT DOUBLE NOT NULL,
        RP integer NOT NULL,
        id integer PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE
    )""")
    conn.commit()
    conn.close()

def insert_users(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username,password))
    c.execute("INSERT INTO AOO (LRL, URL, APW, AA) VALUES (?,?,?,?)", (60,120,0.4,3.5))
    c.execute("INSERT INTO VOO (LRL, URL, VPW, VA) VALUES (?,?,?,?)", (60,120,0.4,3.5))
    c.execute("INSERT INTO AAI (LRL, URL, APW, AA, AT, RP) VALUES (?,?,?,?,?,?)", (60,120,0.4,3.5,3.75,250))
    c.execute("INSERT INTO VVI (LRL, URL, VPW, VA, VT, RP) VALUES (?,?,?,?,?,?)", (60,120,0.4,3.5,3.75,320))
    conn.commit()
    conn.close()

def list_users():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    results = c.fetchall()
    conn.close()
    return results

def list_parameters(mode='AOO'):
    conn = create_connection()
    c = conn.cursor()
    if (mode == "AOO"):
        c.execute("SELECT * FROM AOO")
    elif (mode == "VOO"):
        c.execute("SELECT * FROM VOO")
    elif (mode == "AAI"):
        c.execute("SELECT * FROM AAI")
    elif (mode == "VVI"):
        c.execute("SELECT * FROM VVI")
    else:
        print("Coding Error Detected: Mode in list_parameter(mode) is not recognized")
        return False
    results = c.fetchall()
    conn.close()
    return results

#Delete for production
def main():
    create_database()
    print(list_users())
    print("AOO Data: ", list_parameters("AOO"))
    print("VOO Data: ", list_parameters("VOO"))
    print("AAI Data: ", list_parameters("AAI"))
    print("VVI Data: ", list_parameters("VVI"))

main()
