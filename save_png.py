from PySide2.QtGui import QGuiApplication
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QImage
from PySide2.QtCore import QSize
def save_it(chartview,w,h):
    pixmap = chartview.grab().scaled(QSize(w,h))
    image = pixmap.toImage()
    image.save("test.png")

