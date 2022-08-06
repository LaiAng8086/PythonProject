from importlib.abc import PathEntryFinder
from PySide2.QtCore import QPointF
from PySide2.QtCore import Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QScreen
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QObject
from PySide2.QtCore import SIGNAL
from PySide2.QtCore import QTime
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *
from functools import partial
import random
import csv_read
import time
import copy


class my_normal_chart(QObject):
    def __init__(self, chart_view, pnt, ui):
        super().__init__()
        self.chart = QtCharts.QChart()
        self.cv = chart_view
        self.parent_frame = pnt
        self.size_type = False
        self.formx = 0
        self.formy = 0
        self.posx = 0
        self.posy = 0
        self.ui = ui

    def change_size(self):
        if(not self.size_type):
            self.formx = self.parent_frame.frameSize().width()
            self.formy = self.parent_frame.frameSize().height()
            self.posx = self.parent_frame.x()
            self.posy = self.parent_frame.y()
            self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
            self.parent_frame.setGeometry(0, 0, self.ui.stackedWidget.frameSize().width(),
                                          self.ui.stackedWidget.frameSize().height())
            self.parent_frame.raise_()
            self.size_type = True
        else:
            self.parent_frame.setGeometry(
                self.posx, self.posy, self.formx, self.formy)
            self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
            self.size_type = False

    def finish_draw(self, anime=True):
        self.chart.setTheme(QtCharts.QChart.ChartThemeQt)
        if(anime):
            self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.cv.setRenderHint(QPainter.Antialiasing)
        self.cv.setChart(self.chart)


class my_pie_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.pie = QtCharts.QPieSeries()
        self.pie.clicked.connect(self.change_size)

    def load_data(self, type, data):
        n = len(type)
        for i in range(n):
            new_slice = QtCharts.QPieSlice()
            new_slice.setLabel(type[i]+" "+str(round(data[i]*100, 4))+"%")
            new_slice.setValue(data[i])
            new_slice.setLabelVisible(True)
            self.pie.append(new_slice)

    def finish_draw(self):
        self.chart.addSeries(self.pie)
        self.chart.legend().hide()
        super().finish_draw()


class my_bar_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.bar = QtCharts().QBarSeries()
        self.types = QtCharts.QBarCategoryAxis()
        self.values = QtCharts.QValueAxis()
        self.bar.clicked.connect(self.change_size)
        self.type2 = False

    def load_data(self, groups_name, groups_data):
        n = len(groups_name)
        self.values.setRange(0, 10)
        self.types.append(groups_name)
        for i in range(n):
            new_barset = QtCharts.QBarSet(groups_name[i])
            for j in groups_data[i]:
                new_barset.append(j)
            self.bar.append(new_barset)

    def load_data2(self, groups_name, groups_data):
        self.type2 = True
        self.types.append(groups_name)
        cnt = 0
        self.barset = QtCharts.QBarSet("students")
        self.barset.setColor(QColor("indigo"))
        for i in groups_data:
            cnt += 1
            self.types.append(str(cnt))
            self.barset.append(i)
        self.bar.append(self.barset)
        self.types.setVisible(False)
        print(cnt)

    def change_size(self):
        super().change_size()
        # if(self.type2):
        #     chart_width = self.cv.frameSize().width()
        #     print(chart_width, self.bar.count())
        #     self.bar.setBarWidth(chart_width/self.bar.count())

    def finish_draw(self):
        self.chart.addSeries(self.bar)
        self.chart.addAxis(self.types, Qt.AlignBottom)
        self.chart.addAxis(self.values, Qt.AlignLeft)
        # if(self.type2):
        #     self.chart.legend().hide()
        #     chart_width = self.cv.frameSize().width()
        #     print(chart_width, self.bar.count())
        #     self.bar.setBarWidth(chart_width/self.bar.count())
        super().finish_draw()
        if(self.type2):
            self.barset.setColor(QColor('indigo'))


class my_line_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.line = QtCharts().QLineSeries()
        self.x = QtCharts().QValueAxis()
        self.y = QtCharts().QValueAxis()

    def load_data(self, dataX, dataY):
        n = len(dataX)
        for i in range(n):
            self.line.append(dataX[i], dataY[i])

    def finish_draw(self):
        self.chart.addSeries(self.line)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.x)
        self.chart.setAxisY(self.y)
        super().finish_draw()


def setLine_example(gv):
    chart = my_line_chart(gv)
    n = random.randint(1, 10)
    x = []
    y = []
    for i in range(n):
        x.append(random.randint(3, 10))
        y.append(random.randint(2, 20))
    x.sort()
    chart.load_data(x, y)
    chart.axis_x().setRange(0, 10)
    chart.axis_y().setRange(0, 20)
    chart.finish_draw()
