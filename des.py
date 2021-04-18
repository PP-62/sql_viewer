from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(214, 191)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 131, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineHost = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineHost.setObjectName("lineHost")
        self.verticalLayout.addWidget(self.lineHost)
        self.lineLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineLogin.setObjectName("lineLogin")
        self.verticalLayout.addWidget(self.lineLogin)
        self.lineDBname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineDBname.setClearButtonEnabled(False)
        self.lineDBname.setObjectName("lineDBname")
        self.verticalLayout.addWidget(self.lineDBname)
        self.linePassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.linePassword.setObjectName("linePassword")
        self.verticalLayout.addWidget(self.linePassword)
        self.continueBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.continueBtn.setObjectName("continueBtn")
        self.verticalLayout.addWidget(self.continueBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineHost.setPlaceholderText(_translate("Form", "host..."))
        self.lineLogin.setPlaceholderText(_translate("Form", "login..."))
        self.lineDBname.setPlaceholderText(_translate("Form", "db_name..."))
        self.linePassword.setPlaceholderText(_translate("Form", "password..."))
        self.continueBtn.setText(_translate("Form", "Continue"))
