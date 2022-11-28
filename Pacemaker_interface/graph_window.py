import numpy as np
from numpy import ndarray
from pyqtgraph import PlotWidget, PlotDataItem, mkPen

class GraphWindow(PlotWidget):
    _atrial_data: ndarray #pin a0
    _ventricular_data: ndarray #pin a1
    _atrial_plot: PlotDataItem
    _ventricular_plot: PlotDataItem
    _atr_on: bool
    _vent_on: bool

    def __init__(self, parent=None):
        super().__init__(parent)
        self._atrial_data = np.array([])
        self._ventricular_data = np.array([])
        self._atrial_plot = self.plot(pen=mkPen('r', width=3))
        self._ventricular_plot = self.plot(pen=mkPen('b', width=3))
        self.showGrid(x=True, y=True)
        self.setLabel('left', 'Voltage', units='V')
        self.setLabel('bottom', 'Time', units='s')
        self.setYRange(0, 5)
        self.setXRange(0, 10)
        self._plot

    def _plot(self):
        if self.EGram_comboBox.currentText() == "Atrial Data":   
            self._atrial_plot.setData(self._atrial_data)
            self._ventricular_plot.clear()
        elif self.EGram_comboBox.currentText() == "Ventricular Data": 
            self._atrial_plot.clear()
            self._ventricular_plot.setData(self._ventricular_data)
        else:
            self
        period = 10
        if self._atrial_data <= 400:
            length = len(self._atrial_data)
            x = np.arange(0, length)
            self._atrial_plot.setData(x, self._atrial_data)
            self._ventricular_plot.setData(x, self._ventricular_data)
            length = length/period
            if length % 5 == 0:
                self.setXRange(0, length)
        else:
            x = np.arange(self.index - 400, self.index)/period
            self._atrial_plot.setData(x, self._atrial_data)
            self._ventricular_plot.setData(x, self._ventricular_data)
        self.maxvals += 1
        
    def update(self, atrial_voltage: float, ventricular_voltage: float):
        if self.maxvals <= 400:
            self._atrial_data = np.append(self._atrial_data, atrial_voltage)
            self._ventricular_data = np.append(self._ventricular_data, ventricular_voltage)
        else:
            self._atri_data = np.roll(self._atrial_data, -1)
            self._ventricular_data = np.roll(self._ventricular_data, -1)
            self._atrial_data[-1] = atrial_voltage
            self._ventricular_data[-1] = ventricular_voltage
        self._plot()
    
    def clear(self):
        self._atrial_data = np.array([])
        self._ventricular_data = np.array([])
        self.maxvals = 0
        self._plot()


    