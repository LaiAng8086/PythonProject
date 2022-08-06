from numpy import isin
from save_png import save_it
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
    total = csv_read.select_data(ui.combo_aca.currentText(),
                                 ui.combo_class.currentText(),
                                 ui.combo_nation.currentText(),
                                 ui.combo_sex.currentText(),
                                 ui.combo_factor.currentText())
    ui.combo_aca.setEnabled(False)
    ui.combo_class.setEnabled(False)
    ui.combo_nation.setEnabled(False)
    ui.combo_sex.setEnabled(False)
    ui.combo_factor.setEnabled(False)
    chart_type = ui.combo_chart_type.currentText() 
    if(chart_type=="Pie Chart"):
        show_chart = ui_chart.my_pie_chart(ui.pg2_gv1,ui.frame_8,ui)
        num_len = len(csv_read.selected_num)
        for i in range(num_len):
            csv_read.selected_num[i] /= total
        show_chart.load_data(csv_read.selected_name,csv_read.selected_num)
        show_chart.finish_draw()
    else:
        show_chart = ui_chart.my_bar_chart(ui.pg2_gv1,ui.frame_8,ui)
        show_chart.load_data2(csv_read.selected_name,csv_read.selected_num)
        show_chart.finish_draw()
    ui.combo_aca.setEnabled(True)
    ui.combo_class.setEnabled(True)
    ui.combo_nation.setEnabled(True)
    ui.combo_sex.setEnabled(True)
    ui.combo_factor.setEnabled(True)
        

def export_png():
    if(not had_generated):
        QMessageBox.critical(ui.centralwidget, "Error!",
                             "Please generated first!")
    save_it(ui.pg2_gv1,1440,900)


def setup_button_event():
    ui.Btn_generate.clicked.connect(generate_chart)
    ui.Btn_export.clicked.connect(export_png)
