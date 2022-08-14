import numpy as np
import pandas
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pickletools import uint1
import csv_read
import matplotlib
matplotlib.use("Qt5Agg")


def get_ui(input):
    global ui
    ui = input


class Figure_Canvas(FigureCanvas):

    def __init__(self, title, projection_name=None):
        self.fig = Figure(layout='tight')
        FigureCanvas.__init__(self, self.fig)
        if(projection_name == None):
            self.axes = self.fig.add_subplot(111)
        else:
            self.axes = self.fig.add_subplot(111, projection=projection_name)
        self.axes.legend(('1', '2', '3'), loc='best')
        self.axes.set_title(title)


def setup_diagrams():
    csv_read.read_data()
    fig_1 = Figure_Canvas("Impact Of Relation On Class")
    pandas.crosstab(index=csv_read.csv_data['Relation'], columns=[
                    csv_read.csv_data['Class']], normalize='columns').plot(kind='bar', stacked=True, ax=fig_1.axes)
    ui.page3_grid1.addWidget(fig_1)

    fig_2 = Figure_Canvas("Impact Of Raised Hands On Class")
    csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                     == 1].plot(kind='kde', label="1", ax=fig_2.axes)
    csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                     == 2].plot(kind='kde', label="2", ax=fig_2.axes)
    csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                     == 3].plot(kind='kde', label="3", ax=fig_2.axes)
    fig_2.axes.legend(frameon=False)
    ui.page3_grid2.addWidget(fig_2)

    fig_3 = Figure_Canvas("Impact Of Visited Resources On Class")
    csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                          == 1].plot(kind='kde', label="1", ax=fig_3.axes)
    csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                          == 2].plot(kind='kde', label="2", ax=fig_3.axes)
    csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                          == 3].plot(kind='kde', label="3", ax=fig_3.axes)
    fig_3.axes.legend(frameon=False)
    ui.page3_grid3.addWidget(fig_3)

    fig_4 = Figure_Canvas("Impact Of AnnouncementsView On Class")
    csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                           == 1].plot(kind='kde', label="1", ax=fig_4.axes)
    csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                           == 2].plot(kind='kde', label="2", ax=fig_4.axes)
    csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                           == 3].plot(kind='kde', label="3", ax=fig_4.axes)
    fig_4.axes.legend(frameon=False)
    ui.page3_grid4.addWidget(fig_4)

    fig_5 = Figure_Canvas("Impact Of Discussion On Class")
    csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                    == 1].plot(kind='kde', label="1", ax=fig_5.axes)
    csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                    == 2].plot(kind='kde', label="2", ax=fig_5.axes)
    csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                    == 3].plot(kind='kde', label="3", ax=fig_5.axes)
    fig_5.axes.legend(frameon=False)
    ui.page3_grid5.addWidget(fig_5)

    fig_6 = Figure_Canvas("Impact Of ParentAnsweringSurvey On Class")
    pandas.crosstab(index=csv_read.csv_data['ParentAnsweringSurvey'], columns=[
                    csv_read.csv_data['Class']], normalize='columns').plot(kind='bar', stacked=True, ax=fig_6.axes)
    ui.page3_grid6.addWidget(fig_6)

    fig_7 = Figure_Canvas("Impact Of ParentschoolSatisfaction")
    pandas.crosstab(index=csv_read.csv_data['ParentschoolSatisfaction'], columns=[
                    csv_read.csv_data['Class']], normalize='columns').plot(kind='bar', stacked=True, ax=fig_7.axes)
    ui.page3_grid7.addWidget(fig_7)

    fig_8 = Figure_Canvas("Impact Of StudentAbsenceDays")
    pandas.crosstab(index=csv_read.csv_data['StudentAbsenceDays'], columns=[
                    csv_read.csv_data['Class']], normalize='columns').plot(kind='bar', stacked=True, ax=fig_8.axes)
    ui.page3_grid8.addWidget(fig_8)


def setup_radar():
    fig_radar = Figure_Canvas("Contribution Of Factors On Class", 'polar')
    name = ['StudentAbsenceDays', 'VisitedResources', 'raisedhands',
            'ParentAnsweringSurvey', 'ParentschoolSatisfaction']
    theta = np.linspace(0, 2*np.pi, len(name), endpoint=False)  # 将圆根据标签的个数等比分
    value = np.array([0.635367, 0.124029, 0.083288,
                     0.089499, 0.039189])
    theta = np.concatenate((theta, [theta[0]]))  # 闭合
    value = np.concatenate((value, [value[0]]))  # 闭合
    name = np.concatenate((name, [name[0]]))

    fig_radar.axes.plot(theta, value, color='green', marker='o',
                        lw=2, alpha=0.75, aa=True)  # lw for linewidth
    fig_radar.axes.fill(theta, value, 'b', alpha=0.75)
    fig_radar.axes.set_thetagrids(theta*180/np.pi, name)
    fig_radar.axes.set_yticks(
        [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    fig_radar.axes.set_ylim(0, 1)
    fig_radar.axes.set_theta_zero_location('N')
    fig_radar.axes.legend(frameon=False)

    ui.grid_radar.addWidget(fig_radar)
