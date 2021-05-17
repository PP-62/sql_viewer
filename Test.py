from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pymysql import Connection
from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from connect import Connect

# pyuic5 gui.ui -o gui.py
 
 
class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)

        self.Connect_button.pressed.connect(self.create_connect)
        self.table_select.activated[str].connect(self.select_table)

        self.wrong_connect.setText("")

        self.host_input.setText("localhost")
        self.user_input.setText("root")
        self.password_input.setText("test_db_password_123")
        self.database_input.setText("world")

        self.connection = None
    
    def create_connect(self):
        host = self.host_input.text()
        user = self.user_input.text()
        password = self.password_input.text()
        db = self.database_input.text()
        print(host,user,password,db)
        
        try:
            self.connection = Connect(host,user,password,db)
            self.wrong_connect.setText("Good connect!")
        except:
            self.wrong_connect.setText("Wrong connection!")
        if self.connection:
            self.info_label.setText("host: %s |user: %s |password: %s |db: %s" % (self.connection.host,self.connection.user,self.connection.password,self.connection.db))
            tables = self.connection.get_table_names()
            # print(tables)
            self.table_select.clear()
            for table in tables:
                self.table_select.addItem(table[0])

    def select_table(self, table_name):
        print(table_name)
        if self.connection:
            table = self.connection.get_table(table_name)
            self.table.clear()
            self.table.setRowCount(len(table))
            self.table.setColumnCount(len(table[0]))
            for i in range(len(table)):
                for j in range(len(table[0])):
                    self.table.setItem(i,j, QTableWidgetItem(table[i][j]))
            pass
 
app = QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())