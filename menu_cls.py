import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QErrorMessage
from PyQt5.uic import loadUi
from des import *

class Check(QDialog):
    def __init__(self):
        super(Check, self).__init__()
        loadUi('sql_viewer_design.ui', self)
        self.continueBtn.clicked.connect(self.check_function)

    
    def check_function(self):
        login = self.lineLogin.text()
        password = self.linePassword.text()
        db_name = self.lineDBname.text()
        host = self.lineHost.text()
        error_msg = QtWidgets.QErrorMessage()
        if login == '':
            QMessageBox.critical(self, "Ошибка ", "Неправильно заполнены данные", QMessageBox.Ok)
        elif password == '':
            QMessageBox.critical(self, "Ошибка ", "Неправильно заполнены данные", QMessageBox.Ok) 
        elif db_name == '':
            QMessageBox.critical(self, "Ошибка ", "Неправильно заполнены данные", QMessageBox.Ok)
        elif host == '':
            QMessageBox.critical(self, "Ошибка ", "Неправильно заполнены данные", QMessageBox.Ok)
        else:
            print('Все норм')
        print(f'Login: {login}\nPassword: {password}\nDB_Name: {db_name}\nhost: {host}')

app = QApplication(sys.argv)
mainwindow = Check()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(200)
widget.setFixedWidth(200)
widget.show()
app.exec_()