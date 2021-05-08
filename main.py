from PyQt5 import QtWidgets # import PyQt5 widgets
from PyQt5.QtWidgets import QWidget

from mainwindow import Ui_MainWindow
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
