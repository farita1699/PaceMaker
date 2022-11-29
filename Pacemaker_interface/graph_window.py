import numpy as np
from numpy import ndarray
from pyqtgraph import PlotWidget, PlotDataItem

class GraphWindow(PlotWidget):
    _atrial_data: ndarray #pin a0
    _ventricular_data: ndarray #pin a1
    _atrial_plot: PlotDataItem
    _ventricular_plot: PlotDataItem
    _atr_on: bool
    _vent_on: bool

    def __init__(self, plot: PlotWidget):
        # self._atrial_plot = self.plot(pen=mkPen('r', width=3))
        # self._ventricular_plot = self.plot(pen=mkPen('b', width=3))
        print("Graphs handler init")
        
        plot.showGrid(x=True, y=True)
        plot.setLabel('left', 'Voltage', units='V')
        plot.setLabel('bottom', 'Time', units='s')
        plot.setYRange(0, 5)
        plot.setXRange(0, 10)

        # Initialize graphs to 0
        self._atrial_data = np.array([])
        self._ventricular_data = np.array([])
        self.maxvals = 0

        self._atrial_plot = plot.plot(pen=(0, 229, 255))
        # self._ventricular_plot = plot.plot(pen=(255, 255, 255))
        self._plot()


    def _plot(self):
        time_period = 10
        a_plot_wid = self._atrial_plot.getViewWidget()
        a_plot_wid.disableAutoRange()

        # v_plot_wid = self._ventricular_plot.getViewWidget()
        # v_plot_wid.disableAutoRange()
        if self.maxvals <= 400:
            size = len(self._atrial_data)
            x = np.arange(0, size) / time_period
            a_plot_wid.plot()
            # v_plot_wid.plot()
            self._atrial_plot.setData(x, self._atrial_data)
            # self._ventricular_plot.setData(x, self._ventricular_data)
            size = size/time_period
            if size % 5 == 0:
                a_plot_wid.setXRange(size-4,size+6)
                a_plot_wid.enableAutoRange(x=False, y=True)

                # v_plot_wid.setXRange(size-4,size+6)
                # v_plot_wid.enableAutoRange(x=False, y=True)
        else:
            x = np.arange(self.maxvals - 400, self.maxvals) / time_period
            self._atrial_plot.setData(x, self._atrial_data)
            # self._ventricular_plot.setData(x, self._ventricular_data)
            position = self.maxvals/time_period
            if position % 5 == 0:
                a_plot_wid.setXRange(position-4,position+6)
                a_plot_wid.enableAutoRange(x=False, y=True)

                # v_plot_wid.setXRange(size-4,size+6)
                # v_plot_wid.enableAutoRange(x=False, y=True)
        self.maxvals = self.maxvals + 1
        
    def update(self, atrial_voltage: float, ventricular_voltage: float):
        #print(atrial_voltage, ventricular_voltage)
        if self.maxvals <= 400:
            self._atrial_data = np.append(self._atrial_data, atrial_voltage)
            self._ventricular_data = np.append(self._ventricular_data, ventricular_voltage)
        else:
            self._atrial_data = np.roll(self._atrial_data, -1)
            self._ventricular_data = np.roll(self._ventricular_data, -1)
            self._atrial_data[-1] = atrial_voltage
            self._ventricular_data[-1] = ventricular_voltage
        self._plot()
    
    def clear(self):
        self._atrial_data = np.array([])
        self._ventricular_data = np.array([])
        self.maxvals = 0
        self._plot()


    