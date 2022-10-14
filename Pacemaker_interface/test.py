from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
import mysql.connector
import sys

#Test file for running different test scripts

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle('Hellow World')
    win.show()
    sys.exit(app.exec_())

db = mysql.connector.connect(
    host="pacemaker-aws.cefpanbxdbio.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="admin123",
    database="pacemakerdatabase"
)

mycursor = db.cursor()
# query = "ALTER TABLE users \
#         MODIFY userID int PRIMARY KEY AUTO_INCREMENT"
# mycursor.execute("SHOW DATABASES")
# mycursor.execute(query)

mycursor.execute("INSERT INTO users (username, password) VALUES (%s,%s)", ("Test","Test"))
db.commit()
mycursor.execute("SELECT username FROM users")
# mycursor.execute("DESCRIBE users")   

for x in mycursor:
  print(x)


print("Test")
