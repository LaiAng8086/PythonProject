import sys
from PySide2.QtWidgets import *
import ui_style
import ui_chart
from functools import partial
from Custom_Widgets.Widgets import *
import csv_read
import ui_page_1
import ui_page_2
import load_in
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
    parent_frames = [
        ui.frame_11,
        ui.frame_12,
        ui.frame_13,
        ui.frame_14,
        ui.frame_15,
        ui.frame_16,
        ui.frame_17,
        ui.frame_18,
        ui.frame_19,
        ui.frame_20,
        ui.frame_21,
        ui.frame_22,
        ui.frame_23,
        ui.frame_24,
        ui.frame_25,
        ui.frame_26
    ]
    csv_read.read_csv()
    # ui_chart.setChart_Page1(chartviews)
    ui_page_1.setup(chartviews, parent_frames, ui)
    ui_page_2.get_ui(ui)
    ui_page_2.setup_button_event()
    load_in.get_ui(ui)
    load_in.setup_event()
    loadJsonStyle(MainWindow, ui)
    ui.stackedWidget.setCurrentIndex(0)
    MainWindow.show()
    app.exec_()
