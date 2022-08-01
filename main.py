import sys
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
    chartviews = [
        ui.pg1_gv1,
        ui.pg1_gv2,
        ui.pg1_gv3,
        ui.pg1_gv4,
        ui.pg1_gv5,
        ui.pg1_gv6,
        ui.pg1_gv7,
        ui.pg1_gv8,
        ui.pg1_gv9,
        ui.pg1_gv10,
        ui.pg1_gv11,
        ui.pg1_gv12,
        ui.pg1_gv13,
        ui.pg1_gv14,
        ui.pg1_gv15,
        ui.pg1_gv16
    ]
    ui_chart.setChart_Page1(chartviews)
    loadJsonStyle(MainWindow, ui)
    MainWindow.show()
    sys.exit(app.exec_())
