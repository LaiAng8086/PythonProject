from PySide6.QtCharts import *
from PySide6.QtCore import QPointF
from PySide6.QtCore import Qt
import random


def setChart(gv):
    # Set Series
    series1 = QScatterSeries()
    seq = []
    for i in range(100):
        seq.append(QPointF(i, random.randint(1, 100)))
    series1.append(seq)
    series1.setMarkerShape(QScatterSeries.MarkerShapeCircle)
    series1.setName("Test1")
    series1.setMarkerSize(10.0)
    # Set axis
    axis1 = QValueAxis()
    axis1.setMax(101)
    axis1.setMin(0)
    axis1.setLabelFormat("t")
    # Set Chart
    chart1 = QChart()
    chart1.addSeries(series1)
    chart1.createDefaultAxes()
    chart1.setTheme(QChart.ChartTheme.ChartThemeBlueNcs)
    chart1.setAnimationOptions(QChart.AllAnimations)
    # chart1.addAxis(axis1, Qt.AlignBottom)
    gv.setChart(chart1)
