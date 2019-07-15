# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
from multiprocessing import Process

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_friend_msgBox(object):
    def setupUi(self, friend_msgBox):
        friend_msgBox.setObjectName("friend_msgBox")
        friend_msgBox.resize(704, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        friend_msgBox.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(friend_msgBox)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 360, 681, 148))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.message_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.message_button.setObjectName("message_button")
        self.gridLayout_2.addWidget(self.message_button, 0, 1, 1, 1)
        self.ssh_text = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.ssh_text.setObjectName("ssh_text")
        self.gridLayout_2.addWidget(self.ssh_text, 3, 0, 1, 1)
        self.message_text = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.message_text.setObjectName("message_text")
        self.gridLayout_2.addWidget(self.message_text, 0, 0, 1, 1)
        self.ssh_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ssh_button.setObjectName("ssh_button")
        self.gridLayout_2.addWidget(self.ssh_button, 3, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(470, 10, 221, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.name_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_text.setObjectName("name_text")
        self.gridLayout.addWidget(self.name_text, 1, 1, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastName_label.setObjectName("lastName_label")
        self.gridLayout.addWidget(self.lastName_label, 2, 0, 1, 1)
        self.control_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.control_label.setObjectName("control_label")
        self.gridLayout.addWidget(self.control_label, 5, 0, 1, 1)
        self.motherBoard_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motherBoard_label.setObjectName("motherBoard_label")
        self.gridLayout.addWidget(self.motherBoard_label, 4, 0, 1, 1)
        self.control_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.control_text.setObjectName("control_text")
        self.gridLayout.addWidget(self.control_text, 5, 1, 1, 1)
        self.motherBoard_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motherBoard_text.setObjectName("motherBoard_text")
        self.gridLayout.addWidget(self.motherBoard_text, 4, 1, 1, 1)
        self.ip_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 3, 0, 1, 1)
        self.ip_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ip_text.setObjectName("ip_text")
        self.gridLayout.addWidget(self.ip_text, 3, 1, 1, 1)
        self.allowControl_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.allowControl_label.setObjectName("allowControl_label")
        self.gridLayout.addWidget(self.allowControl_label, 6, 0, 1, 1)
        self.lastName_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastName_text.setObjectName("lastName_text")
        self.gridLayout.addWidget(self.lastName_text, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 1, 1, 1)
        """
        self.chat_text = QtWidgets.QListView(self.centralwidget)
        self.chat_text.setGeometry(QtCore.QRect(10, 10, 451, 341))
        self.chat_text.setObjectName("chat_text")
        """
        self.chat_text = QtWidgets.QListWidget(self.centralwidget)
        self.chat_text.setObjectName("chat_text")
        self.chat_text.setGeometry(QtCore.QRect(10, 10, 451, 341))
        friend_msgBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(friend_msgBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 22))
        self.menubar.setObjectName("menubar")
        friend_msgBox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(friend_msgBox)
        self.statusbar.setObjectName("statusbar")
        friend_msgBox.setStatusBar(self.statusbar)

        self.retranslateUi(friend_msgBox)
        QtCore.QMetaObject.connectSlotsByName(friend_msgBox)

    def retranslateUi(self, friend_msgBox):
        _translate = QtCore.QCoreApplication.translate
        friend_msgBox.setWindowTitle(_translate("friend_msgBox", "chat with"))
        self.message_button.setText(_translate("friend_msgBox", "Send Message"))
        self.ssh_button.setText(_translate("friend_msgBox", "Send SSH Command"))
        self.name_label.setText(_translate("friend_msgBox", "Name:"))
        self.name_text.setText(_translate("friend_msgBox", "-----"))
        self.lastName_label.setText(_translate("friend_msgBox", "Last Name:"))
        self.control_label.setText(_translate("friend_msgBox", "Control:"))
        self.motherBoard_label.setText(_translate("friend_msgBox", "Mother Board:"))
        self.control_text.setText(_translate("friend_msgBox", "Not Alowed"))
        self.motherBoard_text.setText(_translate("friend_msgBox", "-----"))
        self.ip_label.setText(_translate("friend_msgBox", "ip:"))
        self.ip_text.setText(_translate("friend_msgBox", "-----"))
        self.allowControl_label.setText(_translate("friend_msgBox", "Allow Control:"))
        self.lastName_text.setText(_translate("friend_msgBox", "-----"))
        self.label_13.setText(_translate("friend_msgBox", "Friend Details:"))


    def __init__(self,user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id
        self.app = QtWidgets.QApplication(sys.argv)
        self.friend_msgBox = QtWidgets.QMainWindow()
        self.setupUi(self.friend_msgBox)

        def get_messages_process(user_id , friend_id):
            from multiprocessing.pool import ThreadPool
            import client.Get as cg
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(cg.get_messages, (user_id, friend_id))  # tuple of args for foo
            # do some other stuff in the main process
            return_val = async_result.get()  # get the return value from your function.
            return return_val

        self.messages = get_messages_process(user_id , friend_id)
        for msg in self.messages:
            self.chat_text.addItem(msg[0]+" : "+msg[1])



    def open(self):
        self.friend_msgBox.show()
        sys.exit(self.app.exec_())



if __name__ == '__main__':
    #for the testing of the page only:
    #x = Ui_mainWindow(sys.argv[1])s
    default_id1 = '87'
    default_id2 = '99'
    try:
        x = Ui_friend_msgBox(sys.argv[1] , sys.argv[2])
    except:
        x = Ui_friend_msgBox(default_id1 , default_id2)

    print(x.messages)

    x.open()