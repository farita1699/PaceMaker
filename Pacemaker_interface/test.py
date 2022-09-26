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
    host="localhost",
    user="root",
    passwd="root",
    database="pacemakerdatabase"
)

mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")


for x in mycursor:
  print(x)


print("Test")
window()
