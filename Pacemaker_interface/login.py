# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pacemaker_interface/ui/pacemaker_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from frontend.main import Main
from backend.login import check_duplicate, create_new_user, login_check, check_exceed_max_users, check_new_password

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1400, 1000)
        LoginForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        LoginForm.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 270, 751, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.PaceMakerLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PaceMakerLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
"border: 3px solid;\n"
"border-radius: 15px;\n"
"border-color: rgb(232, 232, 232);\n"
"font-size: 80px;")
        self.PaceMakerLabel.setObjectName("PaceMakerLabel")
        self.horizontalLayout_2.addWidget(self.PaceMakerLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UsernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.UsernameLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
"font-size: 50px;")
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.verticalLayout_2.addWidget(self.UsernameLabel)
        self.UsernameInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.UsernameInput.setStyleSheet("height: 40px;\n"
"color: rgb(255, 255, 255);")
        self.UsernameInput.setObjectName("UsernameInput")
        self.verticalLayout_2.addWidget(self.UsernameInput)
        self.PasswordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PasswordLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
"font-size: 50px;")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.verticalLayout_2.addWidget(self.PasswordLabel)
        self.PasswordInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PasswordInput.setStyleSheet("height: 40px;\n"
"color: rgb(255, 255, 255);")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.verticalLayout_2.addWidget(self.PasswordInput)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Register = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Register.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;\n"
"height: 50px;")
        self.Register.setObjectName("Register")
        self.horizontalLayout.addWidget(self.Register)
        self.Login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Login.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;\n"
"height: 50px;")
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        LoginForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginForm)
        self.statusbar.setObjectName("statusbar")
        LoginForm.setStatusBar(self.statusbar)
        self.actionHello_world = QtWidgets.QAction(LoginForm)
        self.actionHello_world.setObjectName("actionHello_world")

        self.Register.clicked.connect(self.register)
        self.Login.clicked.connect(self.login)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def show_register_popup(self, input):
        msg = QMessageBox()
        msg.setWindowTitle("PaceMaker")
        if (input == 1):
            msg.setText("Duplicate username detected")
        elif (input == 2):
            msg.setText("Duplicate username detected")
        elif(input == 3):
            msg.setText("Inappropriate Password")
        else:
            msg.setText("Test")
        x = msg.exec_()

    def register(self):
        if (check_duplicate(self.UsernameInput.text())):
            #To do: make this an error text on the UI
            print("Duplicate detected")
            self.show_register_popup(1)
        elif(check_exceed_max_users()):
            print("Exceed max users")
            self.show_register_popup(2)
        elif(check_new_password(self.PasswordInput.text())):
            print("Inappropriate Password")
            self.show_register_popup(3)
        else:
            create_new_user(self.UsernameInput.text(), self.PasswordInput.text())   

    def login(self):
        if (login_check(self.UsernameInput.text(), self.PasswordInput.text())):
            self.main = Main()
            self.main.show()
            print("Successful")

         
    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "MainWindow"))
        self.PaceMakerLabel.setText(_translate("LoginForm", "PaceMaker"))
        self.UsernameLabel.setText(_translate("LoginForm", "UserName"))
        self.PasswordLabel.setText(_translate("LoginForm", "Password"))
        self.Register.setText(_translate("LoginForm", "Register"))
        self.Login.setText(_translate("LoginForm", "Log In"))
        self.actionHello_world.setText(_translate("LoginForm", "Hello world :)"))
