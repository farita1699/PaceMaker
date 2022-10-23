import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication
)

from UI_MainWindow import UI_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = ui_chris_dashboard()
        self.ui.setupUi(self.main_win)

    def show(self):
        self.main_win.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

    
