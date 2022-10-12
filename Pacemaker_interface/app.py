'''
This file imports many modules from the PyQt.5 environment to generate a GUI. The last few lines define an 
Application, and a Window (with size, title, and ability to exit).

The benefit of the PyQt environment is to generate well-formatted code for Graphical Interfaces given a 
custom build in PyQt Designer, a graphical user interface designer. 
PyQt is able to generate Python code from Qt Designer. As we do not need to distribute the GUI commercially,
we determined this environment to suit our front-end needs.
'''

import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_window import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


    