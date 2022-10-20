from login import Ui_LoginForm
from PyQt5.QtWidgets import QMainWindow

class Window(QMainWindow, Ui_LoginForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)