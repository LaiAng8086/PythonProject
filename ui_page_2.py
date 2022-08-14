from numpy import isin
from save_png import save_it
import ui_chart
import csv_read
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCharts import *


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


show_chart = None


def generate_chart():
    if(ui.combo_factor.currentText() == "------"):
        QMessageBox.critical(ui.centralwidget, "Error!",
                             "Factor must be chosen!")
        return
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
    if(total == 0):
        QMessageBox.critical(ui.centralwidget, "Error!",
                             "No data satisfy the demands constrained by filters.Please set the filters again.")
    else:
        factor_now = ui.combo_factor.currentText()
        global show_chart
        if(chart_type == "Pie Chart"):
            show_chart = ui_chart.my_pie_chart(ui.pg2_gv1, ui.frame_8, ui)
            num_len = len(csv_read.selected_num)
            for i in range(num_len):
                csv_read.selected_num[i] /= total
            show_chart.load_data(csv_read.selected_name, csv_read.selected_num)
            show_chart.finish_draw()
        else:
            show_chart = ui_chart.my_bar_chart(ui.pg2_gv1, ui.frame_8, ui)
            id = csv_read.factor_col[factor_now]
            if(not(id == 8 or id == 13 or id == 14 or id == 15)):
                num_len = len(csv_read.selected_num)
                for i in range(num_len):
                    csv_read.selected_num[i] /= total
                show_chart.values.setTitleText("Probability")
                show_chart.types.setTitleText(factor_now+" times")
                show_chart.load_data2(csv_read.selected_name,
                                      csv_read.selected_num)
            else:
                show_chart.allow = True
                show_chart.values.setTitleText("Count")
                temp = []
                for i in csv_read.selected_num:
                    new_series = []
                    new_series.append(i)
                    temp.append(new_series)
                show_chart.load_data(csv_read.selected_name, temp)
            show_chart.bar.setLabelsPosition(
                QtCharts.QAbstractBarSeries.LabelsInsideEnd)
            show_chart.values.setRange(0, max(csv_read.selected_num))
            show_chart.finish_draw()
        ui.status_label.setText("Status: There are " +
                                str(total)+" records filtered.")
        show_chart.chart.setTitle(factor_now)
    ui.combo_aca.setEnabled(True)
    ui.combo_class.setEnabled(True)
    ui.combo_nation.setEnabled(True)
    ui.combo_sex.setEnabled(True)
    ui.combo_factor.setEnabled(True)


def setup_button_event():
    ui.Btn_generate.clicked.connect(generate_chart)


def setup_default_diagram():
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(8)
    font.setBold(False)
    global default_diagram
    default_diagram = ui_chart.my_bar_chart(
        ui.pg2_gv1, ui.frame_8, ui)
    mmax = default_diagram.load_data(
        csv_read.class_name, csv_read.class_num)
    default_diagram.values.setRange(0, mmax)
    default_diagram.values.setTickInterval(5)
    default_diagram.chart.setTitle("Class Division")
    default_diagram.chart.setFont(font)
    default_diagram.finish_draw()
