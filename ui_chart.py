from PySide2.QtCore import QPointF
from PySide2.QtCore import Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
import random


class my_normal_chart():
    def __init__(self, chart_view):
        self.cv = chart_view
        self.chart = QtCharts.QChart()

    def finish_draw(self):
        self.chart.setTheme(QtCharts.QChart.ChartThemeBlueNcs)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.cv.setRenderHint(QPainter.Antialiasing)
        self.cv.setChart(self.chart)


class my_pie_chart(my_normal_chart):
    def __init__(self, chart_view):
        super().__init__(chart_view)
        self.pie = QtCharts.QPieSeries()
        self.pie.setLabelsPosition(QtCharts.QPieSlice.LabelInsideNormal)

    def load_data(self,  type, data):
        n = len(type)
        for i in range(n):
            new_slice = QtCharts.QPieSlice()
            new_slice.setLabel(type[i]+" "+str(data[i]*100)+"%")
            new_slice.setValue(data[i])
            new_slice.setLabelVisible(True)
            new_slice.setBorderWidth(10)
            self.pie.append(new_slice)

    def finish_draw(self):
        self.chart.addSeries(self.pie)
        self.chart.legend().hide()
        super().finish_draw()


class my_bar_chart(my_normal_chart):
    def __init__(self, chart_view):
        super().__init__(chart_view)
        self.bar = QtCharts().QBarSeries()
        self.types = QtCharts.QBarCategoryAxis()
        self.values = QtCharts.QValueAxis()

    def load_data(self, groups_name, groups_data):
        n = len(groups_name)
        self.values.setRange(0, 10)
        self.types.append(groups_name)
        for i in range(n):
            new_barset = QtCharts.QBarSet(groups_name[i])
            for j in groups_data[i]:
                new_barset.append(j)
            self.bar.append(new_barset)

    def finish_draw(self):
        self.chart.addSeries(self.bar)
        self.chart.addAxis(self.types, Qt.AlignBottom)
        self.chart.addAxis(self.values, Qt.AlignLeft)
        super().finish_draw()


class my_line_chart(my_normal_chart):
    def __init__(self, chart_view):
        super().__init__(chart_view)
        self.line = QtCharts().QLineSeries()
        self.x = QtCharts().QValueAxis()
        self.y = QtCharts().QValueAxis()

    def load_data():
        pass


def setBar_example(gv):
    chart = my_bar_chart(gv)
    groups_name = ['A', 'B', 'C', 'D', 'E']
    groups_data = [[] for i in range(5)]
    for i in range(5):
        for j in range(5):
            groups_data[i].append(random.randint(0, 10))
    chart.load_data(groups_name, groups_data)
    chart.finish_draw()


def setPie_example(gv):
    chart = my_pie_chart(gv)
    n = random.randint(1, 6)
    ratio = []
    label = []
    for i in range(n):
        label.append(chr(random.randint(40, 127)))
        ratio.append(random.randint(1, 20))
    chart.load_data(label, ratio)
    chart.finish_draw()


def setChart_Page1(chartviews):
    for i in chartviews:
        coin = random.random()
        if coin > 0.5:
            setBar_example(i)
        else:
            setPie_example(i)


def setChart_Page2(gv):
    # Set Series
    series1 = QtCharts.QScatterSeries()
    seq = []
    for i in range(100):
        seq.append(QPointF(i, random.randint(1, 100)))
    series1.append(seq)
    series1.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeCircle)
    series1.setName("Test1")
    series1.setMarkerSize(10.0)
    # Set axis
    axis1 = QtCharts.QValueAxis()
    axis1.setMax(101)
    axis1.setMin(0)
    axis1.setLabelFormat("t")
    # Set Chart
    chart1 = QtCharts.QChart()
    chart1.addSeries(series1)
    chart1.createDefaultAxes()
    chart1.setTheme(QtCharts.QChart.ChartTheme.ChartThemeDark)
    chart1.setAnimationOptions(QtCharts.QChart.AllAnimations)
    # chart1.addAxis(axis1, Qt.AlignBottom)
    gv.setChart(chart1)
