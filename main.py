import sys
from PySide6.QtWidgets import *
import ui_style
import ui_chart

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_style.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui_chart.setChart(ui.graphicsView)
    ui_chart.setChart(ui.graphicsView_2)
    MainWindow.show()
    sys.exit(app.exec_())
