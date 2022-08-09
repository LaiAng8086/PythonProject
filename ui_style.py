# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts
from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu

import files_rc
import svg_files_rc
import icons_2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"font: 75 9pt \"Comic Sans MS\";\n"
"color: rgb(210, 210, 210);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_leftmenu = QCustomSlideMenu(self.frame_main)
        self.widget_leftmenu.setObjectName(u"widget_leftmenu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_leftmenu.sizePolicy().hasHeightForWidth())
        self.widget_leftmenu.setSizePolicy(sizePolicy)
        self.widget_leftmenu.setMinimumSize(QSize(0, 0))
        self.widget_leftmenu.setMaximumSize(QSize(1677215, 16777215))
        self.widget_leftmenu.setStyleSheet(u"background-color: rgb(0, 0, 139);\n"
"font: 15pt \"Comic Sans MS\";")
        self.verticalLayout = QVBoxLayout(self.widget_leftmenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_leftmenu)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 0, 128);\n"
"	border-radius: 5px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(25, 25, 112);\n"
"	border: 2px solid rgb(65, 105, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(72, 61, 139);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Btn_1 = QPushButton(self.frame_4)
        self.Btn_1.setObjectName(u"Btn_1")
        sizePolicy.setHeightForWidth(self.Btn_1.sizePolicy().hasHeightForWidth())
        self.Btn_1.setSizePolicy(sizePolicy)
        self.Btn_1.setMaximumSize(QSize(16777215, 50))
        self.Btn_1.setFont(font)
        self.Btn_1.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/All/icons_2/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_1.setIcon(icon)
        self.Btn_1.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.Btn_1)

        self.Btn_2 = QPushButton(self.frame_4)
        self.Btn_2.setObjectName(u"Btn_2")
        sizePolicy.setHeightForWidth(self.Btn_2.sizePolicy().hasHeightForWidth())
        self.Btn_2.setSizePolicy(sizePolicy)
        self.Btn_2.setMaximumSize(QSize(16777215, 50))
        icon1 = QIcon()
        icon1.addFile(u":/All/icons_2/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_2.setIcon(icon1)
        self.Btn_2.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.Btn_2)

        self.Btn_3 = QPushButton(self.frame_4)
        self.Btn_3.setObjectName(u"Btn_3")
        sizePolicy.setHeightForWidth(self.Btn_3.sizePolicy().hasHeightForWidth())
        self.Btn_3.setSizePolicy(sizePolicy)
        self.Btn_3.setMaximumSize(QSize(16777215, 50))
        self.Btn_3.setFont(font)
        self.Btn_3.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/All/icons_2/flag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_3.setIcon(icon2)
        self.Btn_3.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.Btn_3)

        self.Btn_4 = QPushButton(self.frame_4)
        self.Btn_4.setObjectName(u"Btn_4")
        sizePolicy.setHeightForWidth(self.Btn_4.sizePolicy().hasHeightForWidth())
        self.Btn_4.setSizePolicy(sizePolicy)
        self.Btn_4.setMaximumSize(QSize(16777215, 50))
        self.Btn_4.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/All/icons_2/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_4.setIcon(icon3)
        self.Btn_4.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.Btn_4)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 0, 128);\n"
"	border-radius: 5px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(25, 25, 112);\n"
"	border: 2px solid rgb(65, 105, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(72, 61, 139);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.toolButton = QToolButton(self.frame_5)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMaximumSize(QSize(16777215, 30))
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"	border: 2px solid rgb(0, 0, 128);\n"
"	border-radius: 5px;	\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(25, 25, 112);\n"
"	border: 2px solid rgb(65, 105, 225);\n"
"}\n"
"QToolButton:pressed {	\n"
"	background-color: rgb(72, 61, 139);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_4.addWidget(self.toolButton, 1, 1, 1, 1)

        self.label_filepath = QLabel(self.frame_5)
        self.label_filepath.setObjectName(u"label_filepath")
        self.label_filepath.setStyleSheet(u"font: 10pt \"Times Newman\";")

        self.gridLayout_4.addWidget(self.label_filepath, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 75 12pt \"Comic Sans MS\";")

        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 2)

        self.Btn_import = QPushButton(self.frame_5)
        self.Btn_import.setObjectName(u"Btn_import")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_import.sizePolicy().hasHeightForWidth())
        self.Btn_import.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.Btn_import, 2, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.widget_leftmenu)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setStyleSheet(u"background-color: rgb(135, 206, 250);")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_content)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_top)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 130, 180);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Btn_toggle = QPushButton(self.frame_9)
        self.Btn_toggle.setObjectName(u"Btn_toggle")
        self.Btn_toggle.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/All/icons_2/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_toggle.setIcon(icon4)
        self.Btn_toggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.Btn_toggle)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Comic Sans MS\";")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_header = QFrame(self.frame_top)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_header)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 13pt \"Comic Sans MS\";")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_header)

        self.frame_2 = QFrame(self.frame_top)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 130, 180);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 139);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Btn_minimize = QPushButton(self.frame_2)
        self.Btn_minimize.setObjectName(u"Btn_minimize")
        self.Btn_minimize.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/20x20/icons/20x20/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_minimize.setIcon(icon5)
        self.Btn_minimize.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.Btn_minimize)

        self.Btn_maximize = QPushButton(self.frame_2)
        self.Btn_maximize.setObjectName(u"Btn_maximize")
        self.Btn_maximize.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/20x20/icons/20x20/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_maximize.setIcon(icon6)
        self.Btn_maximize.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.Btn_maximize)

        self.Btn_close = QPushButton(self.frame_2)
        self.Btn_close.setObjectName(u"Btn_close")
        self.Btn_close.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/20x20/icons/20x20/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close.setIcon(icon7)
        self.Btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.Btn_close)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_top)

        self.frame_views = QFrame(self.frame_content)
        self.frame_views.setObjectName(u"frame_views")
        sizePolicy2.setHeightForWidth(self.frame_views.sizePolicy().hasHeightForWidth())
        self.frame_views.setSizePolicy(sizePolicy2)
        self.frame_views.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.frame_views.setFrameShape(QFrame.StyledPanel)
        self.frame_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_views)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomStackedWidget(self.frame_views)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(8, 0, 8, 0)
        self.frame_25 = QFrame(self.frame_10)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_25)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pg1_label15 = QLabel(self.frame_25)
        self.pg1_label15.setObjectName(u"pg1_label15")

        self.verticalLayout_23.addWidget(self.pg1_label15, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv15 = QtCharts.QChartView(self.frame_25)
        self.pg1_gv15.setObjectName(u"pg1_gv15")

        self.verticalLayout_23.addWidget(self.pg1_gv15)


        self.gridLayout_3.addWidget(self.frame_25, 3, 2, 1, 1)

        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pg1_label8 = QLabel(self.frame_18)
        self.pg1_label8.setObjectName(u"pg1_label8")

        self.verticalLayout_16.addWidget(self.pg1_label8, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv8 = QtCharts.QChartView(self.frame_18)
        self.pg1_gv8.setObjectName(u"pg1_gv8")

        self.verticalLayout_16.addWidget(self.pg1_gv8)


        self.gridLayout_3.addWidget(self.frame_18, 1, 3, 1, 1)

        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pg1_label12 = QLabel(self.frame_22)
        self.pg1_label12.setObjectName(u"pg1_label12")

        self.verticalLayout_20.addWidget(self.pg1_label12, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv12 = QtCharts.QChartView(self.frame_22)
        self.pg1_gv12.setObjectName(u"pg1_gv12")

        self.verticalLayout_20.addWidget(self.pg1_gv12)


        self.gridLayout_3.addWidget(self.frame_22, 2, 3, 1, 1)

        self.frame_23 = QFrame(self.frame_10)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pg1_label13 = QLabel(self.frame_23)
        self.pg1_label13.setObjectName(u"pg1_label13")

        self.verticalLayout_21.addWidget(self.pg1_label13, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv13 = QtCharts.QChartView(self.frame_23)
        self.pg1_gv13.setObjectName(u"pg1_gv13")

        self.verticalLayout_21.addWidget(self.pg1_gv13)


        self.gridLayout_3.addWidget(self.frame_23, 3, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_24)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pg1_label14 = QLabel(self.frame_24)
        self.pg1_label14.setObjectName(u"pg1_label14")

        self.verticalLayout_22.addWidget(self.pg1_label14, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv14 = QtCharts.QChartView(self.frame_24)
        self.pg1_gv14.setObjectName(u"pg1_gv14")

        self.verticalLayout_22.addWidget(self.pg1_gv14)


        self.gridLayout_3.addWidget(self.frame_24, 3, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pg1_label4 = QLabel(self.frame_14)
        self.pg1_label4.setObjectName(u"pg1_label4")

        self.verticalLayout_12.addWidget(self.pg1_label4, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv4 = QtCharts.QChartView(self.frame_14)
        self.pg1_gv4.setObjectName(u"pg1_gv4")

        self.verticalLayout_12.addWidget(self.pg1_gv4)


        self.gridLayout_3.addWidget(self.frame_14, 0, 3, 1, 1)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pg1_label9 = QLabel(self.frame_19)
        self.pg1_label9.setObjectName(u"pg1_label9")

        self.verticalLayout_17.addWidget(self.pg1_label9, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv9 = QtCharts.QChartView(self.frame_19)
        self.pg1_gv9.setObjectName(u"pg1_gv9")

        self.verticalLayout_17.addWidget(self.pg1_gv9)


        self.gridLayout_3.addWidget(self.frame_19, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pg1_label2 = QLabel(self.frame_12)
        self.pg1_label2.setObjectName(u"pg1_label2")

        self.verticalLayout_10.addWidget(self.pg1_label2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv2 = QtCharts.QChartView(self.frame_12)
        self.pg1_gv2.setObjectName(u"pg1_gv2")

        self.verticalLayout_10.addWidget(self.pg1_gv2)


        self.gridLayout_3.addWidget(self.frame_12, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pg1_label7 = QLabel(self.frame_17)
        self.pg1_label7.setObjectName(u"pg1_label7")

        self.verticalLayout_15.addWidget(self.pg1_label7, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv7 = QtCharts.QChartView(self.frame_17)
        self.pg1_gv7.setObjectName(u"pg1_gv7")

        self.verticalLayout_15.addWidget(self.pg1_gv7)


        self.gridLayout_3.addWidget(self.frame_17, 1, 2, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pg1_label1 = QLabel(self.frame_11)
        self.pg1_label1.setObjectName(u"pg1_label1")

        self.verticalLayout_9.addWidget(self.pg1_label1, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv1 = QtCharts.QChartView(self.frame_11)
        self.pg1_gv1.setObjectName(u"pg1_gv1")

        self.verticalLayout_9.addWidget(self.pg1_gv1)


        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_20)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pg1_label10 = QLabel(self.frame_20)
        self.pg1_label10.setObjectName(u"pg1_label10")

        self.verticalLayout_18.addWidget(self.pg1_label10, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv10 = QtCharts.QChartView(self.frame_20)
        self.pg1_gv10.setObjectName(u"pg1_gv10")

        self.verticalLayout_18.addWidget(self.pg1_gv10)


        self.gridLayout_3.addWidget(self.frame_20, 2, 1, 1, 1)

        self.frame_26 = QFrame(self.frame_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pg1_label16 = QLabel(self.frame_26)
        self.pg1_label16.setObjectName(u"pg1_label16")

        self.verticalLayout_24.addWidget(self.pg1_label16, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv16 = QtCharts.QChartView(self.frame_26)
        self.pg1_gv16.setObjectName(u"pg1_gv16")

        self.verticalLayout_24.addWidget(self.pg1_gv16)


        self.gridLayout_3.addWidget(self.frame_26, 3, 3, 1, 1)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pg1_label6 = QLabel(self.frame_16)
        self.pg1_label6.setObjectName(u"pg1_label6")

        self.verticalLayout_14.addWidget(self.pg1_label6, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv6 = QtCharts.QChartView(self.frame_16)
        self.pg1_gv6.setObjectName(u"pg1_gv6")

        self.verticalLayout_14.addWidget(self.pg1_gv6)


        self.gridLayout_3.addWidget(self.frame_16, 1, 1, 1, 1)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pg1_label5 = QLabel(self.frame_15)
        self.pg1_label5.setObjectName(u"pg1_label5")

        self.verticalLayout_13.addWidget(self.pg1_label5, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv5 = QtCharts.QChartView(self.frame_15)
        self.pg1_gv5.setObjectName(u"pg1_gv5")

        self.verticalLayout_13.addWidget(self.pg1_gv5)


        self.gridLayout_3.addWidget(self.frame_15, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pg1_label11 = QLabel(self.frame_21)
        self.pg1_label11.setObjectName(u"pg1_label11")

        self.verticalLayout_19.addWidget(self.pg1_label11, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv11 = QtCharts.QChartView(self.frame_21)
        self.pg1_gv11.setObjectName(u"pg1_gv11")

        self.verticalLayout_19.addWidget(self.pg1_gv11)


        self.gridLayout_3.addWidget(self.frame_21, 2, 2, 1, 1)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pg1_label3 = QLabel(self.frame_13)
        self.pg1_label3.setObjectName(u"pg1_label3")

        self.verticalLayout_11.addWidget(self.pg1_label3, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pg1_gv3 = QtCharts.QChartView(self.frame_13)
        self.pg1_gv3.setObjectName(u"pg1_gv3")

        self.verticalLayout_11.addWidget(self.pg1_gv3)


        self.gridLayout_3.addWidget(self.frame_13, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_10, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_33 = QLabel(self.frame_6)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 0, 6, 1, 1, Qt.AlignHCenter)

        self.combo_factor = QComboBox(self.frame_6)
        self.combo_factor.setObjectName(u"combo_factor")

        self.gridLayout.addWidget(self.combo_factor, 3, 5, 1, 1)

        self.label_34 = QLabel(self.frame_6)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 0, 5, 1, 1, Qt.AlignHCenter)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1, Qt.AlignHCenter)

        self.combo_nation = QComboBox(self.frame_6)
        self.combo_nation.setObjectName(u"combo_nation")

        self.gridLayout.addWidget(self.combo_nation, 3, 3, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1, Qt.AlignHCenter)

        self.combo_sex = QComboBox(self.frame_6)
        self.combo_sex.setObjectName(u"combo_sex")

        self.gridLayout.addWidget(self.combo_sex, 3, 4, 1, 1)

        self.combo_chart_type = QComboBox(self.frame_6)
        self.combo_chart_type.setObjectName(u"combo_chart_type")

        self.gridLayout.addWidget(self.combo_chart_type, 3, 6, 1, 1)

        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 0, 1, 1, 1, Qt.AlignHCenter)

        self.combo_class = QComboBox(self.frame_6)
        self.combo_class.setObjectName(u"combo_class")

        self.gridLayout.addWidget(self.combo_class, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1, Qt.AlignHCenter)

        self.combo_aca = QComboBox(self.frame_6)
        self.combo_aca.setObjectName(u"combo_aca")

        self.gridLayout.addWidget(self.combo_aca, 3, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 10pt \"Times New Roman\";")

        self.verticalLayout_33.addWidget(self.label)

        self.Btn_generate = QPushButton(self.frame_3)
        self.Btn_generate.setObjectName(u"Btn_generate")

        self.verticalLayout_33.addWidget(self.Btn_generate)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pg2_gv1 = QtCharts.QChartView(self.frame_8)
        self.pg2_gv1.setObjectName(u"pg2_gv1")

        self.horizontalLayout_7.addWidget(self.pg2_gv1)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_8 = QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.page_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grid_radar = QGridLayout()
        self.grid_radar.setObjectName(u"grid_radar")

        self.verticalLayout_4.addLayout(self.grid_radar)


        self.horizontalLayout_9.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QSize(525, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_29)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 248, 3100))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.page3_frame1 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame1.setObjectName(u"page3_frame1")
        self.page3_frame1.setMinimumSize(QSize(0, 400))
        self.page3_frame1.setFrameShape(QFrame.StyledPanel)
        self.page3_frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.page3_frame1)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.page3_frame1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_27.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.page3_grid1 = QGridLayout()
        self.page3_grid1.setObjectName(u"page3_grid1")

        self.verticalLayout_27.addLayout(self.page3_grid1)


        self.verticalLayout_25.addWidget(self.page3_frame1)

        self.page3_frame2 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame2.setObjectName(u"page3_frame2")
        self.page3_frame2.setMinimumSize(QSize(0, 400))
        self.page3_frame2.setFrameShape(QFrame.StyledPanel)
        self.page3_frame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.page3_frame2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.page3_frame2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_28.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.page3_grid2 = QGridLayout()
        self.page3_grid2.setObjectName(u"page3_grid2")

        self.verticalLayout_28.addLayout(self.page3_grid2)


        self.verticalLayout_25.addWidget(self.page3_frame2)

        self.page3_frame3 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame3.setObjectName(u"page3_frame3")
        self.page3_frame3.setMinimumSize(QSize(0, 300))
        self.page3_frame3.setFrameShape(QFrame.StyledPanel)
        self.page3_frame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.page3_frame3)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.page3_frame3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_29.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.page3_grid3 = QGridLayout()
        self.page3_grid3.setObjectName(u"page3_grid3")

        self.verticalLayout_29.addLayout(self.page3_grid3)


        self.verticalLayout_25.addWidget(self.page3_frame3)

        self.page3_frame4 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame4.setObjectName(u"page3_frame4")
        self.page3_frame4.setMinimumSize(QSize(0, 400))
        self.page3_frame4.setFrameShape(QFrame.StyledPanel)
        self.page3_frame4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.page3_frame4)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.page3_frame4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_30.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.page3_grid4 = QGridLayout()
        self.page3_grid4.setObjectName(u"page3_grid4")

        self.verticalLayout_30.addLayout(self.page3_grid4)


        self.verticalLayout_25.addWidget(self.page3_frame4)

        self.page3_frame5 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame5.setObjectName(u"page3_frame5")
        self.page3_frame5.setMinimumSize(QSize(0, 400))
        self.page3_frame5.setFrameShape(QFrame.StyledPanel)
        self.page3_frame5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.page3_frame5)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.page3_frame5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_31.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.page3_grid5 = QGridLayout()
        self.page3_grid5.setObjectName(u"page3_grid5")

        self.verticalLayout_31.addLayout(self.page3_grid5)


        self.verticalLayout_25.addWidget(self.page3_frame5)

        self.page3_frame6 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame6.setObjectName(u"page3_frame6")
        self.page3_frame6.setMinimumSize(QSize(0, 400))
        self.page3_frame6.setFrameShape(QFrame.StyledPanel)
        self.page3_frame6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.page3_frame6)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.page3_frame6)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_35.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.page3_grid6 = QGridLayout()
        self.page3_grid6.setObjectName(u"page3_grid6")

        self.verticalLayout_35.addLayout(self.page3_grid6)


        self.verticalLayout_25.addWidget(self.page3_frame6)

        self.page3_frame7 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame7.setObjectName(u"page3_frame7")
        sizePolicy.setHeightForWidth(self.page3_frame7.sizePolicy().hasHeightForWidth())
        self.page3_frame7.setSizePolicy(sizePolicy)
        self.page3_frame7.setMinimumSize(QSize(0, 400))
        self.page3_frame7.setFrameShape(QFrame.StyledPanel)
        self.page3_frame7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.page3_frame7)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.impact_label_1 = QLabel(self.page3_frame7)
        self.impact_label_1.setObjectName(u"impact_label_1")

        self.verticalLayout_26.addWidget(self.impact_label_1, 0, Qt.AlignHCenter)

        self.page3_grid7 = QGridLayout()
        self.page3_grid7.setSpacing(0)
        self.page3_grid7.setObjectName(u"page3_grid7")

        self.verticalLayout_26.addLayout(self.page3_grid7)


        self.verticalLayout_25.addWidget(self.page3_frame7)

        self.page3_frame8 = QFrame(self.scrollAreaWidgetContents)
        self.page3_frame8.setObjectName(u"page3_frame8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page3_frame8.sizePolicy().hasHeightForWidth())
        self.page3_frame8.setSizePolicy(sizePolicy3)
        self.page3_frame8.setMinimumSize(QSize(0, 400))
        self.page3_frame8.setFrameShape(QFrame.StyledPanel)
        self.page3_frame8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.page3_frame8)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.page3_frame8)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_36.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.page3_grid8 = QGridLayout()
        self.page3_grid8.setObjectName(u"page3_grid8")

        self.verticalLayout_36.addLayout(self.page3_grid8)


        self.verticalLayout_25.addWidget(self.page3_frame8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.horizontalLayout_9.addWidget(self.frame_29)


        self.horizontalLayout_8.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_10 = QHBoxLayout(self.page_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.page_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.page4_grid = QGridLayout()
        self.page4_grid.setObjectName(u"page4_grid")

        self.verticalLayout_32.addLayout(self.page4_grid)


        self.horizontalLayout_10.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_views)

        self.frame_bottom = QFrame(self.frame_content)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.frame_bottom)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 0);")

        self.horizontalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.status_label = QLabel(self.frame_bottom)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setStyleSheet(u"font: 13pt \"Times New Roman\";")

        self.horizontalLayout_11.addWidget(self.status_label)

        self.Btn_export = QPushButton(self.frame_bottom)
        self.Btn_export.setObjectName(u"Btn_export")
        self.Btn_export.setEnabled(False)
        self.Btn_export.setStyleSheet(u"QPushButton:disabled{\n"
"	color: rgb(109,109,109)\n"
"}")

        self.horizontalLayout_11.addWidget(self.Btn_export)


        self.verticalLayout_3.addWidget(self.frame_bottom)


        self.horizontalLayout_2.addWidget(self.frame_content)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_1.setText(QCoreApplication.translate("MainWindow", u"Data Summary", None))
        self.Btn_2.setText(QCoreApplication.translate("MainWindow", u"Score Analysis", None))
        self.Btn_3.setText(QCoreApplication.translate("MainWindow", u"Feature Analysis", None))
        self.Btn_4.setText(QCoreApplication.translate("MainWindow", u"Feature Correlation", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_filepath.setText(QCoreApplication.translate("MainWindow", u"- - - - - -", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Choose the data file to load", None))
        self.Btn_import.setText(QCoreApplication.translate("MainWindow", u"Import!", None))
        self.Btn_toggle.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data Visualization Toolkit", None))
        self.Btn_minimize.setText("")
        self.Btn_maximize.setText("")
        self.Btn_close.setText("")
        self.pg1_label15.setText(QCoreApplication.translate("MainWindow", u"Absent", None))
        self.pg1_label8.setText(QCoreApplication.translate("MainWindow", u"Relation", None))
        self.pg1_label12.setText(QCoreApplication.translate("MainWindow", u"Parent Survey", None))
        self.pg1_label13.setText(QCoreApplication.translate("MainWindow", u"Parent Satisfaction", None))
        self.pg1_label14.setText(QCoreApplication.translate("MainWindow", u"Announcement", None))
        self.pg1_label4.setText(QCoreApplication.translate("MainWindow", u"School Level", None))
        self.pg1_label9.setText(QCoreApplication.translate("MainWindow", u"Raise Hands", None))
        self.pg1_label2.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.pg1_label7.setText(QCoreApplication.translate("MainWindow", u"Semester", None))
        self.pg1_label1.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.pg1_label10.setText(QCoreApplication.translate("MainWindow", u"Online Resources", None))
        self.pg1_label16.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.pg1_label6.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.pg1_label5.setText(QCoreApplication.translate("MainWindow", u"Academic Year", None))
        self.pg1_label11.setText(QCoreApplication.translate("MainWindow", u"Discussion", None))
        self.pg1_label3.setText(QCoreApplication.translate("MainWindow", u"Birth Place", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Chart Type", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Factor", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Academic Year", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Notice:\n"
" 1. The factor you would like to observe must be set.\n"
" 2. If you choose the default item of a filter, it will not exclude any data for this.", None))
        self.Btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate Diagram!", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Impact Of Relation On Class ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Impact Of Raised Hands On Class", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Impact Of Visited Resources On Class", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Impact Of AnnouncementsView On Class", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Impact Of Discussion On Class", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Impact Of ParentAnsweringSurvey On Class", None))
        self.impact_label_1.setText(QCoreApplication.translate("MainWindow", u"Impact Of ParentschoolSatisfaction", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Impact Of StudentAbsenceDays", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Python Project By jyz,wxg,jrt & ljh!", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status: Data not loaded yet!", None))
        self.Btn_export.setText(QCoreApplication.translate("MainWindow", u"Export to PNG!", None))
    # retranslateUi

