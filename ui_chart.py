from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from importlib.abc import PathEntryFinder
from PySide2.QtCore import QPointF
from PySide2.QtCore import Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import random
import matplotlib
import save_png
matplotlib.use("Qt5Agg")


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
        self.hover_in = False

    def hover_title(self):
        if(not self.hover_in):
            self.hover_in = True
            self.parent_frame.setFrameShadow(QFrame.Plain)
        else:
            self.hover_in = False
            self.parent_frame.setFrameShadow(QFrame.Raised)

    def change_size(self):
        if(not self.size_type):
            # self.ui.Btn_export.setVisible(True)
            self.ui.Btn_export.setDisabled(False)
            save_png.set_chartview(self.cv)
            self.formx = self.parent_frame.frameSize().width()
            self.formy = self.parent_frame.frameSize().height()
            self.posx = self.parent_frame.x()
            self.posy = self.parent_frame.y()
            self.parent_frame.setGeometry(0, 0, self.ui.stackedWidget.frameSize().width(),
                                          self.ui.stackedWidget.frameSize().height())
            self.parent_frame.repaint()
            self.parent_frame.raise_()
            self.size_type = True
        else:
            # self.ui.Btn_export.setVisible(False)
            self.ui.Btn_export.setDisabled(True)
            self.parent_frame.setGeometry(
                self.posx, self.posy, self.formx, self.formy)
            self.parent_frame.repaint()
            self.size_type = False

    def finish_draw(self, anime=True):
        if(anime):
            self.chart.setAnimationDuration(200)
            self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.cv.setRenderHint(QPainter.Antialiasing)
        self.cv.setChart(self.chart)


class my_pie_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.pie = QtCharts.QPieSeries()
        self.pie.hovered.connect(self.hover_title)
        self.pie.clicked.connect(self.change_size)
        self.pie.setLabelsVisible(False)

    def change_size(self):
        super().change_size()
        if(self.size_type == False):
            self.pie.setLabelsVisible(False)
            self.pie.hovered.connect(self.hover_title)
        else:
            self.pie.setLabelsVisible(True)
            self.pie.hovered.disconnect(self.hover_title)

    def set_not_change(self):
        self.pie.clicked.disconnect(self.change_size)

    def load_data(self, type, data):
        n = len(type)
        for i in range(n):
            new_slice = QtCharts.QPieSlice()
            new_slice.setLabel(str(type[i])+" "+str(round(data[i]*100, 2))+"%")
            new_slice.setValue(data[i])
            new_slice.setLabelVisible(True)
            self.pie.append(new_slice)

    def finish_draw(self):
        self.chart.addSeries(self.pie)
        self.chart.legend().hide()
        self.pie.setLabelsVisible(False)
        super().finish_draw()


class my_bar_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.bar = QtCharts().QBarSeries()
        self.types = QtCharts.QCategoryAxis()
        self.values = QtCharts.QValueAxis()
        self.bar.hovered.connect(self.hover_title)
        self.bar.clicked.connect(self.change_size)
        self.type2 = False
        self.allow = False

    def load_data(self, groups_name, groups_data):
        n = len(groups_name)
        ret = 0
        for i in range(n):
            self.types.append(groups_name[i], float(i))
            new_barset = QtCharts.QBarSet(groups_name[i])
            for j in groups_data[i]:
                new_barset.append(j)
                ret = max(ret, j)
            self.bar.append(new_barset)
        return ret

    def load_data2(self, groups_name, groups_data):
        self.type2 = True
        cnt = 0
        self.types.setMin(0)
        self.types.setMax(len(groups_name)+1)
        for i in groups_name:
            cnt += 1
            if(cnt % 5 == 0):
                self.types.append(str(i), float(cnt))
        barset = QtCharts.QBarSet("")
        for i in groups_data:
            barset.append(i)
        self.bar.append(barset)

    def set_not_change(self):
        self.bar.clicked.disconnect(self.change_size)

    def change_size(self):
        super().change_size()
        if(self.size_type == True):
            self.values.setVisible(True)
            if(self.type2):
                self.types.setVisible(True)
                if(self.allow):
                    self.bar.setLabelsVisible(True)
            else:
                self.bar.setLabelsVisible(True)
        else:
            self.values.setVisible(False)
            self.types.setVisible(False)
            self.bar.setLabelsVisible(False)

    def finish_draw(self):
        self.chart.addSeries(self.bar)
        self.chart.addAxis(self.types, Qt.AlignBottom)
        self.chart.addAxis(self.values, Qt.AlignLeft)
        if(not self.type2):
            self.bar.setLabelsPosition(
                QtCharts.QAbstractBarSeries.LabelsInsideEnd)
        self.values.setVisible(False)
        self.types.setVisible(False)
        self.bar.setLabelsVisible(False)
        if(self.type2):
            self.chart.legend().hide()
        super().finish_draw()


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
