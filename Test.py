from PyQt5 import QtWidgets
from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

# pyuic5 gui.ui -o gui.py
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())