from display.main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from backend.login import list_parameters
import time
import config

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def logout(self):
        time.sleep(0.2)
        self.close()
        # self.login = Login()
        # self.login.show()
        

###New code
    def switchMode(self):
        if self.comboBox.currentText() == "AOO":
            self.stackedWidget.setCurrentWidget(self.AOO_Widget)#Might have to do self.ui.AOOWIdget
        elif self.comboBox.currentText() == "VOO":
            self.stackedWidget.setCurrentWidget(self.VOO_Widget)
        elif self.comboBox.currentText() == "AAI":
            self.stackedWidget.setCurrentWidget(self.AAI_Widget)
        elif self.comboBox.currentText() == "VVI":
            self.stackedWidget.setCurrentWidget(self.VVI_Widget)

    def initializeParameters(self):

        self.AOO_LRL_Field.setPlainText(str(config.cache['AOO']['LRL']))
        print(config.cache)

        
        