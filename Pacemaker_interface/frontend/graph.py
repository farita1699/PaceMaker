from display.graph import Ui_Graph
from PyQt5.QtWidgets import QWidget, QMainWindow
from serial_communication import ConnectionHandler
from graph_window import GraphWindow
from database.db import update_parameters, list_parameters
import time

class Graph(QMainWindow, Ui_Graph):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = ConnectionHandler()
        self.graphing = GraphWindow()
        #self.conn.ser.ecg_data_update.connect(self.update_graph)

    def switchPlot(self):
        if self.EGram_comboBox.currentText() == "Atrial Data":
            self.graphing.plot_ecg()