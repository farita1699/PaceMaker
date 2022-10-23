# from main import Ui_Main
from main2 import Ui_Main
from PyQt5.QtWidgets import QMainWindow

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
