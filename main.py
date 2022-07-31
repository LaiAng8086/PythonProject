import sys
import os
from PySide2.QtWidgets import *
import ui_style
import ui_chart
from functools import partial
from Custom_Widgets.Widgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_style.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui_chart.setChart(ui.graphicsView)
    os.chdir(os.getcwd())
    loadJsonStyle(MainWindow,ui)
    MainWindow.show()
    sys.exit(app.exec_())
