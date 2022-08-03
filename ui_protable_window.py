from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCharts import QtCharts
import sys
import time
import copy


class portable_window(QMainWindow):
    def __init__(self, chart):
        super().__init__()
        self.resize(1440, 900)
        self.chartview = QtCharts.QChartView(self)
        chart.cv = self
        self.chartview.setChart(chart)

    def get_chartview(self):
        return self.chartview

    def display(self):
        self.show()
        time.sleep(1)
