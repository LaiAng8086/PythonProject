from numpy import uint
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import ui_page_1
import ui_page_2
import csv_read
def get_ui(input):
    global ui
    ui = input

file_ok=False
def get_file():
    global file_name
    file_name = QFileDialog.getOpenFileName(
        ui.centralwidget, "Open a csv data file", "", "Data File (*.csv)")
    ui.label_filepath.setText(file_name[0])


def import_file():
    ui_page_1.finish_draw_all()
    ui_page_2.setup_combo()
    ui_page_2.setup_default_diagram()
    ui.status_label.setText("Status: There are "+str(csv_read.total_records)+" records in total.")
    QMessageBox.information(ui.centralwidget, "Import",
                            "The file has been imported successfully!")


def setup_event():
    ui.toolButton.clicked.connect(get_file)
    ui.Btn_import.clicked.connect(import_file)
