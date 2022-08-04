from numpy import isin
import ui_chart
import csv_read
from PySide2.QtWidgets import *


def get_ui(input):
    global ui
    ui = input


def setup_combo():
    ui.combo_aca.addItem("------")
    for i in csv_read.academic_name:
        ui.combo_aca.addItem(i)

    ui.combo_class.addItem("------")
    for i in csv_read.class_name:
        ui.combo_class.addItem(i)

    ui.combo_nation.addItem("------")
    for i in csv_read.nation_name:
        ui.combo_nation.addItem(i)

    ui.combo_sex.addItem("------")
    ui.combo_sex.addItem("Boys")
    ui.combo_sex.addItem("Girls")

    ui.combo_factor.addItem("------")
    for i in csv_read.factors:
        ui.combo_factor.addItem(i)

    ui.combo_chart_type.addItem("Pie Chart")
    ui.combo_chart_type.addItem("Bar Chart")


had_generated = False


def generate_chart():
    global had_generated
    had_generated = True


def export_png():
    if(not had_generated):
        QMessageBox.critical(ui.centralwidget, "Error!",
                             "Please generated first!")


def setup_button_event():
    ui.Btn_generate.clicked.connect(generate_chart)
    ui.Btn_export.clicked.connect(export_png)
