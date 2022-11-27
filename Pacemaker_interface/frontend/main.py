from display.main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from serial_communication import ConnectionHandler
from database.db import update_parameters, list_parameters
import time
import config


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = ConnectionHandler()
        self.conn.ser.ecg_data_update.connect(self.test)
        self.conn.ser.params_received.connect(self.test2)

    def test(self):
        print("Test something")

    def test2(self):
        print("Test something else")

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
        #Initialize AOO parameters from the cache
        self.AOO_LRL_Field.setValue(config.cache['AOO']['LRL'])
        self.AOO_URL_Field.setValue(config.cache['AOO']['URL'])
        self.AOO_ATR_PW_FIELD.setValue(config.cache['AOO']['APW'])
        self.AOO_AMP_FIELD.setValue(config.cache['AOO']['AA'])

        #Initialize VOO parameters from the cache
        self.VOO_LRL_Field.setValue(config.cache['VOO']['LRL'])
        self.VOO_URL_Field.setValue(config.cache['VOO']['URL'])
        self.VOO_VENT_PW_FIELD.setValue(config.cache['VOO']['VPW'])
        self.VOO_VENT_AMP_FIELD.setValue(config.cache['VOO']['VA'])

        #Initialize AAI parameters from the cache
        self.AAI_LRL_Field.setValue(config.cache['AAI']['LRL'])
        self.AAI_URL_Field.setValue(config.cache['AAI']['URL'])
        self.AAI_ATR_PW_FIELD.setValue(config.cache['AAI']['APW'])
        self.AAI_ATR_AMP_FIELD.setValue(config.cache['AAI']['AA'])
        self.AAI_ATR_THRESH__FIELD.setValue(config.cache['AAI']['AT'])
        self.AAI_REFRACT_Field.setValue(config.cache['AAI']['RP'])

        #Initialize VVI parameters from the cache
        self.VVI_LRL_Field.setValue(config.cache['VVI']['LRL'])
        self.VVI_URL_Field.setValue(config.cache['VVI']['URL'])
        self.VVI_VENT_PW_FIELD.setValue(config.cache['VVI']['VPW'])
        self.VVI_VENT_AMP_FIELD.setValue(config.cache['VVI']['VA'])
        self.VVI_VENT_THRESH__FIELD.setValue(config.cache['VVI']['VT'])
        self.VVI_REFRACT_Field.setValue(config.cache['VVI']['RP'])
        
    def saveParameters(self):
        #To do: create a backend layer between frontend and database (bad practice to directly call database queries from frontend due to security reasons)
        update_parameters('AOO','LRL',self.AOO_LRL_Field.value(),config.cache['id'])
        update_parameters('AOO','URL',self.AOO_URL_Field.value(),config.cache['id'])
        update_parameters('AOO','APW',self.AOO_ATR_PW_FIELD.value(),config.cache['id'])
        update_parameters('AOO','AA',self.AOO_AMP_FIELD.value(),config.cache['id'])

        update_parameters('VOO','LRL',self.VOO_LRL_Field.value(),config.cache['id'])
        update_parameters('VOO','URL',self.VOO_URL_Field.value(),config.cache['id'])
        update_parameters('VOO','VPW',self.VOO_VENT_PW_FIELD.value(),config.cache['id'])
        update_parameters('VOO','VA',self.VOO_VENT_AMP_FIELD.value(),config.cache['id'])

        update_parameters('AAI','LRL',self.AAI_LRL_Field.value(),config.cache['id'])
        update_parameters('AAI','URL',self.AAI_URL_Field.value(),config.cache['id'])
        update_parameters('AAI','APW',self.AAI_ATR_PW_FIELD.value(),config.cache['id'])
        update_parameters('AAI','AA',self.AAI_ATR_AMP_FIELD.value(),config.cache['id'])
        update_parameters('AAI','AT',self.AAI_ATR_THRESH__FIELD.value(),config.cache['id'])
        update_parameters('AAI','RP',self.AAI_REFRACT_Field.value(),config.cache['id'])

        update_parameters('VVI','LRL',self.VVI_LRL_Field.value(),config.cache['id'])
        update_parameters('VVI','URL',self.VVI_URL_Field.value(),config.cache['id'])
        update_parameters('VVI','VPW',self.VVI_VENT_PW_FIELD.value(),config.cache['id'])
        update_parameters('VVI','VA',self.VVI_VENT_AMP_FIELD.value(),config.cache['id'])
        update_parameters('VVI','VT',self.VVI_VENT_THRESH__FIELD.value(),config.cache['id'])
        update_parameters('VVI','RP',self.VVI_REFRACT_Field.value(),config.cache['id'])

        print("AOO Data: ", list_parameters("AOO"))
        print("VOO Data: ", list_parameters("VOO"))
        print("AAI Data: ", list_parameters("AAI"))
        print("VVI Data: ", list_parameters("VVI"))

    

        
        