import os
from multiprocessing import Process
from threading import Thread
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys


class App(QWidget):
    def message_box(self, friend_name):
        resp = QMessageBox.question(self, 'Approve control', 'Do you approve to ' + friend_name + " to control yours computer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resp == QMessageBox.Yes:
            return True
        else:
            return False

class Ui_friend_msgBox(object):
    def setupUi(self, friend_msgBox):
        friend_msgBox.setObjectName("friend_msgBox")
        friend_msgBox.resize(898, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        friend_msgBox.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(friend_msgBox)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 360, 861, 148))
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(470, 10, 401, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.lastName_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastName_text.setObjectName("lastName_text")
        self.gridLayout.addWidget(self.lastName_text, 2, 1, 1, 1)
        self.control_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.control_label.setObjectName("control_label")
        self.gridLayout.addWidget(self.control_label, 5, 0, 1, 1)
        self.ip_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 3, 0, 1, 1)
        self.ip_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ip_text.setObjectName("ip_text")
        self.gridLayout.addWidget(self.ip_text, 3, 1, 1, 1)
        self.control_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.control_text.setObjectName("control_text")
        self.gridLayout.addWidget(self.control_text, 5, 1, 1, 1)
        self.name_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_text.setObjectName("name_text")
        self.gridLayout.addWidget(self.name_text, 1, 1, 1, 1)
        self.motherBoard_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motherBoard_text.setObjectName("motherBoard_text")
        self.gridLayout.addWidget(self.motherBoard_text, 4, 1, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastName_label.setObjectName("lastName_label")
        self.gridLayout.addWidget(self.lastName_label, 2, 0, 1, 1)
        self.motherBoard_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motherBoard_label.setObjectName("motherBoard_label")
        self.gridLayout.addWidget(self.motherBoard_label, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.ask_for_control_button = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.ask_for_control_button.setObjectName("ask_for_control_button")
        self.gridLayout.addWidget(self.ask_for_control_button, 6, 0, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_2, 6, 1, 1, 1)
        self.chat_text = QtWidgets.QListWidget(self.centralwidget)
        self.chat_text.setGeometry(QtCore.QRect(10, 10, 451, 341))
        self.chat_text.setObjectName("chat_text")
        friend_msgBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(friend_msgBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 22))
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
        self.lastName_text.setText(_translate("friend_msgBox", "-----"))
        self.control_label.setText(_translate("friend_msgBox", "Control:"))
        self.ip_label.setText(_translate("friend_msgBox", "ip:"))
        self.ip_text.setText(_translate("friend_msgBox", "-----"))
        self.control_text.setText(_translate("friend_msgBox", "Not Alowed"))
        self.name_text.setText(_translate("friend_msgBox", "-----"))
        self.motherBoard_text.setText(_translate("friend_msgBox", "-----"))
        self.lastName_label.setText(_translate("friend_msgBox", "Last Name:"))
        self.motherBoard_label.setText(_translate("friend_msgBox", "Mother Board:"))
        self.label_13.setText(_translate("friend_msgBox", "Friend Details:"))
        self.ask_for_control_button.setText(_translate("friend_msgBox", "Ask for Control"))
        self.commandLinkButton_2.setText(_translate("friend_msgBox", "Disable his control"))

    def __init__(self, user_id, user_pass, user_sudo, friend_id):
        from client import user
        self.user_id = user_id
        self.user_password = user_pass
        self.user_sudo = user_sudo
        try:
            self.my_user = my_user = user.User(self.user_id, self.user_password, self.user_sudo)
        except Exception as e:
            print(e)
            self.my_user = my_user = user.User.get_instance()
        self.friend_id = friend_id
        self.app = QtWidgets.QApplication(sys.argv)
        self.friend_msgBox = QtWidgets.QMainWindow()
        self.setupUi(self.friend_msgBox)

        # self.message_text.returnPressed.connect(self.message_button.animateClick)
        def get_msgs_history():
            msgs = my_user.get_message(friend_id)
            print(msgs)
            if msgs:
                for msg in msgs:
                    self.chat_text.addItem(msg[0] + " > " + msg[1])

        get_msgs_history()
        self.motherBoard_text.setText(my_user.get_friend_motherboard(friend_id))

        self.message_button.clicked.connect(self.send_msg)
        self.ask_for_control_button.clicked.connect(self.ask_for_control)
        self.ssh_button.clicked.connect(self.send_ssh_msg)

        def get_messages_process():
            from multiprocessing.pool import ThreadPool
            my_thread_for_simple_msgs = Thread(target=listen_msg)
            my_thread_for_simple_msgs.start()
            my_thread_for_ssh_msgs = Thread(target=listen_to_ssh_msg)
            my_thread_for_ssh_msgs.start()

        def listen_msg():
            while True:
                if len(my_user.my_queue) > 0:
                    data = self.my_user.my_queue.pop()
                    print(self.my_user.id + "  got message from :" + data['sender_id'])
                    if self.friend_id == data['sender_id']:
                        self.chat_text.addItem(data['sender_name'] + " > " + data['text'])

                else:
                    self.my_user.my_queue_waiter.acquire()
                    print("wating...")
                    self.my_user.my_queue_waiter.wait()
                    print("interupted")
                    self.my_user.my_queue_waiter.release()

        def listen_to_ssh_msg():
            while True:
                if len(my_user.ssh_results_command_queue) > 0:
                    data = self.my_user.ssh_results_command_queue.pop()
                    print(self.my_user.id + "  got message from :" + data['sender_id'])
                    if self.friend_id == data['sender_id']:
                        self.chat_text.addItem(data['sender_name'] + " > " + data['text'])

                else:
                    self.my_user.ssh_results_command_queue_waiter.acquire()
                    print("wating...")
                    self.my_user.ssh_results_command_queue_waiter.wait()
                    print("interupted")
                    self.my_user.ssh_results_command_queue_waiter.release()

        def get_control_req_process():
            my_thread = Thread(target=listen_to_control_req)
            my_thread.start()

        def listen_to_control_req():
            while True: #busy waiting
                set_of_req = my_user.approve_control_requests
                if len(set_of_req) > 0 and friend_id in set_of_req:
                    ap = App()
                    ans = ap.message_box(friend_id)
                    if ans:
                        print("yes")
                        my_user.approve_control(friend_id, True)
                    elif not ans:
                        my_user.approve_control(friend_id, False)
                        print("no")
                else:
                    my_user.approve_control_requests_waiter.acquire()
                    my_user.approve_control_requests_waiter.wait()
                    my_user.approve_control_requests_waiter.release()

        get_control_req_process()
        get_messages_process()
        """
        self.messages = get_messages_process(user_id , friend_id)
        for msg in self.messages:
            self.chat_text.addItem(msg[0]+" > "+msg[1])
        """
    def ask_for_control(self):
        self.my_user.ask_for_control(self.friend_id)

    def send_msg(self):
        msg_txt = self.message_text.toPlainText()
        print("my text is " + msg_txt)
        if msg_txt != '':
            self.my_user.send_message(self.friend_id, msg_txt)
            self.message_text.setPlainText("")
            self.chat_text.addItem(self.my_user.name + " > " + msg_txt)

    def send_ssh_msg(self):
        msg_txt = self.ssh_text.toPlainText()
        print("my text is " + msg_txt)
        if msg_txt != '':
            self.my_user.send_ssh_message(self.friend_id, msg_txt)
            self.ssh_text.setPlainText("")
            #self.chat_text.addItem(self.my_user.name + " > " + msg_txt)

    def open(self):
        self.friend_msgBox.show()
        sys.exit(self.app.exec_())



if __name__ == '__main__':
    # for the testing of the page only:
    # x = Ui_mainWindow(sys.argv[1])s
    default_id1 = 'testUser2'
    default_id2 = 'testUser'
    default_pas = '12345'
    default_sudo = '1313'

    try:
        x = Ui_friend_msgBox(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except:
        x = Ui_friend_msgBox(default_id1, default_pas, default_sudo, default_id2)

    # print(x.messages)

    x.open()

