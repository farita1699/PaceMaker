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
        self.graphHandle = GraphWindow(self.plots)

    def update_plot(self, atr, vtr):
        print("Update")
        self.graphHandle.update(atr, vtr)

    def switchPlot(self):
        # if self.EGram_comboBox.currentText() == "Atrial Data":
        #     self.graphing.plot_ecg()
        pass