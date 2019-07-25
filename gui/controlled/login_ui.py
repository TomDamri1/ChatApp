# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from multiprocessing import Process
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../..")
from client import user_login


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(279, 173)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginPage.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        self.username_text = QtWidgets.QLineEdit(self.centralwidget)
        self.username_text.setObjectName("username_text")
        self.gridLayout.addWidget(self.username_text, 0, 1, 1, 1)
        self.username_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.username_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.username_label_2.setObjectName("username_label_2")
        self.gridLayout.addWidget(self.username_label_2, 1, 0, 1, 1)
        self.password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.gridLayout.addWidget(self.password_text, 1, 1, 1, 1)
        self.sudo_password_label = QtWidgets.QLabel(self.centralwidget)
        self.sudo_password_label.setObjectName("sudo_password_label")
        self.gridLayout.addWidget(self.sudo_password_label, 2, 0, 1, 1)
        self.sudo_password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.sudo_password_text.setObjectName("sudo_password_text")
        self.sudo_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.sudo_password_text, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.signup_label = QtWidgets.QLabel(self.centralwidget)
        self.signup_label.setObjectName("signup_label")
        self.gridLayout.addWidget(self.signup_label, 3, 0, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 22))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)
        self.use_server_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.use_server_checkbox.setObjectName("use_server_checkbox")
        self.gridLayout.addWidget(self.use_server_checkbox, 4, 0, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)
        self.username_text.returnPressed.connect(self.password_text.selectAll)
        self.password_text.returnPressed.connect(self.sudo_password_text.selectAll)
        self.sudo_password_text.returnPressed.connect(self.pushButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)
        self.pushButton.clicked.connect(self.login)
        self.use_server_checkbox.clicked.connect(self.switch_url)

    def switch_url(self):
        if self.use_server_checkbox.isChecked():
            path = os.path.expanduser('~')
            path = path + '/url.txt'
            f = open(path, 'w')
            f.write("http://localhost:5000/")
            f.close()
        else:
            path = os.path.expanduser('~')
            path = path + '/url.txt'
            f = open(path, 'w')
            f.write("http://linuxchat.herokuapp.com/")
            f.close()

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Login"))
        self.username_label.setText(_translate("LoginPage", "ID:"))
        self.username_label_2.setText(_translate("LoginPage", "Password:"))
        self.sudo_password_label.setText(_translate("LoginPage", "sudo passowrd:"))
        self.pushButton.setText(_translate("LoginPage", "Login"))
        self.signup_label.setText(_translate("LoginPage", "Sign up!"))
        self.use_server_checkbox.setText(_translate("LoginPage", "Use local server"))

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.LoginPage = QtWidgets.QMainWindow()
        # override a contain object method
        self.LoginPage.closeEvent = self.closeEvent
        self.setupUi(self.LoginPage)
        self.login_flag = False
        self.pushButton.clicked.connect(self.login)
        self.signup_label.mousePressEvent = self.register
        self.signup_label.setStyleSheet("color : blue")
        self.use_server_checkbox.setChecked(False)
        try:
            path = os.path.expanduser('~')
            path = path + '/url.txt'
            print('Path is:' + path)
            f = open(path, 'w')
            print("create")
            f.write("http://linuxchat.herokuapp.com/")
            f.close()
        except:
            print("an error occurred during create url.txt file please contact the developer team.")

    def register(self, *args):
        register_page_process = Process(target=os.system, args=("python3 ../../client/registerUser.py ", ))
        register_page_process.start()


    def open(self):
        try:
            self.LoginPage.show()
        except:
            pass
        sys.exit(self.app.exec_())


    def login(self):
        if self.login_flag == False:
            def enter_main_page(userid , userpass , usersudo):
                string_of_details = str(userid)+ " "+str(userpass) +" " +str (usersudo)
                main_page_process = Process(target= os.system , args=("python3 mainWindow_ui.py "+string_of_details,))
                main_page_process.start()

            '''
            def open_new_socket(userid):
                new_socket_process = Process(target= os.system , args=("python3 ../../client/socketClient.py",))
                new_socket_process.start()
            '''
            user_id = self.user_id = self.username_text.text()
            user_password = self.user_password = self.password_text.text()
            user_sudo = self.user_sudo = self.sudo_password_text.text()
            if self.check_login_details(user_id , user_password , user_sudo):
                self.login_flag = True
                enter_main_page(user_id , user_password , user_sudo)
                self.LoginPage.hide()
                sys.exit(self.app.exec_())


                #open_new_socket(user_id)


    def closeEvent(self, *args):
        print("exit from login window")
        try:
            path = os.path.expanduser('~')
            path = path + '/url.txt'
            os.remove(path)
        except:
            pass

    def check_login_details(self,user_id, user_password, user_sudo_password):
        print("checking detials..")
        my_user = user_login.connect(user_id, user_password, user_sudo_password)
        if isinstance(my_user, str):
            print("wrong username or password")
            return False
        print("authenticated succsesfuly!")
        return True

    def close(self):
        self.app.quit()


if __name__ == '__main__':
    try:
        print("opening login page..")
        def run_login():
            x = Ui_LoginPage()
            x.open()
        login_process = Process(target=run_login)
        print("starting..")
        login_process.start()
        print("started")
    except Exception as e:
        print("we got error")
        pass
