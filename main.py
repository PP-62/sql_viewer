from PyQt5 import QtCore, QtGui, QtWidgets
from menu_cls import *
from des import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Check()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(200)
    widget.setFixedWidth(200)
    widget.show()
    app.exec_()
    sys.exit(app.exec_())