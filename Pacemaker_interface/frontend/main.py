# from main import Ui_Main
from ui_chris_dashboard import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
