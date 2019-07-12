# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
from multiprocessing import Process

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading
from gui.controlled.mainWindow_ui import Ui_mainWindow



class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(333, 237)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginPage.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.gridLayout.addWidget(self.password_text, 1, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        self.username_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.username_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.username_label_2.setObjectName("username_label_2")
        self.gridLayout.addWidget(self.username_label_2, 1, 0, 1, 1)
        self.username_text = QtWidgets.QLineEdit(self.centralwidget)
        self.username_text.setObjectName("username_text")
        self.gridLayout.addWidget(self.username_text, 0, 1, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 22))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        self.username_text.returnPressed.connect(self.password_text.selectAll)
        self.password_text.returnPressed.connect(self.pushButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Login"))
        self.pushButton.setText(_translate("LoginPage", "Login"))
        self.username_label.setText(_translate("LoginPage", "Email:"))
        self.username_label_2.setText(_translate("LoginPage", "Password:"))


    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.LoginPage = QtWidgets.QMainWindow()
        self.setupUi(self.LoginPage)
        self.login_flag = False

    def open(self):
        self.LoginPage.show()
        sys.exit(self.app.exec_())


    def login(self):

        def enter_main_page(userid):
            main_page_process = Process (target= os.system , args=("python3 mainWindow_ui.py "+str(userid),))
            main_page_process.start()

        user_id = self.user_id = self.username_text.text()
        user_password = self.user_password = self.password_text.text()
        print(user_id , user_password)
        if self.check_login_details(user_id , user_password):
            self.login_flag = True
            enter_main_page(user_id)
            self.close()


    def check_login_details(self,user_id,user_password):
        """
        if exists(user_id):
            if getUser(user_id).password == password:
                return True
        return Fasle
        """
        return True

    def close(self):
        self.app.quit()


os.system("pwd")
x = Ui_LoginPage()
x.open()