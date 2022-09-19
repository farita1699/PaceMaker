from PyQt5 import QtWidgets
from PyQt5.QtWidgts import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argy)
    win = QMainWindow()
    win.setGeometry(0, 0, 300, 300)
    win.setWindowTitle('Hellow World')
    sys.exit(app.exec_())