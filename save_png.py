from PySide2.QtGui import QGuiApplication
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QImage
from PySide2.QtCore import QSize
from PySide2.QtCore import *
from PySide2.QtWidgets import *


def set_chartview(input):
    global cv
    cv = input


def get_ui(input):
    global ui
    ui = input


def export_png():
    global ui
    file_name, _ = QFileDialog.getSaveFileName(
        ui.centralwidget, "Save to a png image", "", "PNG File (*.png)")
    print(file_name)
    if(file_name != None):
        global cv
        save_it(cv, 1440, 900, file_name)


def save_it(chartview, w, h, file_name):
    pixmap = chartview.grab().scaled(QSize(w, h))
    image = pixmap.toImage()
    image.save(file_name)
