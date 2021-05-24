# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 10, 131, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.host_input = QtWidgets.QLineEdit(self.frame)
        self.host_input.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.host_input.setText("")
        self.host_input.setObjectName("host_input")
        self.user_input = QtWidgets.QLineEdit(self.frame)
        self.user_input.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.user_input.setObjectName("user_input")
        self.password_input = QtWidgets.QLineEdit(self.frame)
        self.password_input.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.password_input.setObjectName("password_input")
        self.database_input = QtWidgets.QLineEdit(self.frame)
        self.database_input.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.database_input.setObjectName("database_input")
        self.wrong_connect = QtWidgets.QLabel(self.frame)
        self.wrong_connect.setGeometry(QtCore.QRect(10, 160, 111, 31))
        self.wrong_connect.setObjectName("wrong_connect")
        self.connect_button = QtWidgets.QPushButton(self.frame)
        self.connect_button.setGeometry(QtCore.QRect(10, 130, 111, 23))
        self.connect_button.setObjectName("connect_button")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(140, 10, 571, 601))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.info_label = QtWidgets.QLabel(self.frame_2)
        self.info_label.setGeometry(QtCore.QRect(10, 10, 551, 21))
        self.info_label.setObjectName("info_label")
        self.table_select = QtWidgets.QComboBox(self.frame_2)
        self.table_select.setGeometry(QtCore.QRect(40, 40, 161, 22))
        self.table_select.setEditable(False)
        self.table_select.setCurrentText("")
        self.table_select.setObjectName("table_select")
        self.table_label = QtWidgets.QLabel(self.frame_2)
        self.table_label.setGeometry(QtCore.QRect(10, 40, 31, 21))
        self.table_label.setObjectName("table_label")
        self.table = QtWidgets.QTableWidget(self.frame_2)
        self.table.setGeometry(QtCore.QRect(10, 70, 551, 181))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.grafic = GraficWidget(self.frame_2)
        self.grafic.setGeometry(QtCore.QRect(10, 290, 551, 241))
        self.grafic.setObjectName("grafic")
        self.select_column_1 = QtWidgets.QComboBox(self.frame_2)
        self.select_column_1.setGeometry(QtCore.QRect(110, 260, 131, 22))
        self.select_column_1.setObjectName("select_column_1")
        self.select_column_label_1 = QtWidgets.QLabel(self.frame_2)
        self.select_column_label_1.setGeometry(QtCore.QRect(10, 260, 111, 21))
        self.select_column_label_1.setObjectName("select_column_label_1")
        self.select_column_label_2 = QtWidgets.QLabel(self.frame_2)
        self.select_column_label_2.setGeometry(QtCore.QRect(250, 260, 111, 21))
        self.select_column_label_2.setObjectName("select_column_label_2")
        self.select_column_2 = QtWidgets.QComboBox(self.frame_2)
        self.select_column_2.setGeometry(QtCore.QRect(360, 260, 131, 22))
        self.select_column_2.setObjectName("select_column_2")
        self.save_lavel = QtWidgets.QLabel(self.frame_2)
        self.save_lavel.setGeometry(QtCore.QRect(90, 570, 231, 20))
        self.save_lavel.setText("")
        self.save_lavel.setAlignment(QtCore.Qt.AlignCenter)
        self.save_lavel.setObjectName("save_lavel")
        self.execute_button = QtWidgets.QPushButton(self.frame_2)
        self.execute_button.setGeometry(QtCore.QRect(10, 570, 71, 23))
        self.execute_button.setObjectName("execute_button")
        self.select_edit = QtWidgets.QLineEdit(self.frame_2)
        self.select_edit.setGeometry(QtCore.QRect(10, 540, 551, 20))
        self.select_edit.setObjectName("select_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.host_input.setPlaceholderText(_translate("MainWindow", "host:"))
        self.user_input.setPlaceholderText(_translate("MainWindow", "user:"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "password:"))
        self.database_input.setPlaceholderText(_translate("MainWindow", "database:"))
        self.wrong_connect.setText(_translate("MainWindow", "Wrong Conect!"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.info_label.setText(_translate("MainWindow", "info:"))
        self.table_select.setPlaceholderText(_translate("MainWindow", "Tables..."))
        self.table_label.setText(_translate("MainWindow", "Table:"))
        self.select_column_label_1.setText(_translate("MainWindow", "Select first column:"))
        self.select_column_label_2.setText(_translate("MainWindow", "Select second column:"))
        self.execute_button.setText(_translate("MainWindow", "Execute"))
        self.select_edit.setPlaceholderText(_translate("MainWindow", "SELECT..."))
from graficwidget import GraficWidget
