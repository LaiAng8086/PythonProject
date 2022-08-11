from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCharts import *
import csv_read

def get_ui(input):
    global ui
    ui = input


def cur_index():
    now = ui.stackedWidget.currentIndex()
    if(now > 1):
        ui.status_label.setVisible(False)
    else:
        ui.status_label.setVisible(True)
        if(now==0):
            ui.status_label.setText("Status: There are "+str(csv_read.total_records)+" records in total.")
