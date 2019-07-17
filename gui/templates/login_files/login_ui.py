# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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

        self.retranslateUi(LoginPage)
        self.username_text.returnPressed.connect(self.password_text.selectAll)
        self.password_text.returnPressed.connect(self.pushButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Login"))
        self.username_label.setText(_translate("LoginPage", "Email:"))
        self.username_label_2.setText(_translate("LoginPage", "Password:"))
        self.sudo_password_label.setText(_translate("LoginPage", "sudo passowrd:"))
        self.pushButton.setText(_translate("LoginPage", "Login"))
        self.signup_label.setText(_translate("LoginPage", "Sign up!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
