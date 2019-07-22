# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import os
from multiprocessing import Process
import sys
from client import user
from threading import Thread, Condition
import time
friendList = []


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(326, 897)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userDetails_grid = QtWidgets.QGridLayout()
        self.userDetails_grid.setObjectName("userDetails_grid")
        self.motherBoard_label = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_label.setObjectName("motherBoard_label")
        self.userDetails_grid.addWidget(self.motherBoard_label, 5, 1, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.centralwidget)
        self.lastName_label.setObjectName("lastName_label")
        self.userDetails_grid.addWidget(self.lastName_label, 2, 1, 1, 1)
        self.cpu_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_label.setObjectName("cpu_label")
        self.userDetails_grid.addWidget(self.cpu_label, 6, 1, 1, 1)
        self.cpu_text = QtWidgets.QLabel(self.centralwidget)
        self.cpu_text.setObjectName("cpu_text")
        self.userDetails_grid.addWidget(self.cpu_text, 6, 2, 1, 1)
        self.Jtag_text = QtWidgets.QLabel(self.centralwidget)
        self.Jtag_text.setObjectName("Jtag_text")
        self.userDetails_grid.addWidget(self.Jtag_text, 0, 2, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.userDetails_grid.addWidget(self.name_label, 1, 1, 1, 1)
        self.Jtag_label = QtWidgets.QLabel(self.centralwidget)
        self.Jtag_label.setObjectName("Jtag_label")
        self.userDetails_grid.addWidget(self.Jtag_label, 0, 1, 1, 1)
        self.lastName_text = QtWidgets.QLabel(self.centralwidget)
        self.lastName_text.setObjectName("lastName_text")
        self.userDetails_grid.addWidget(self.lastName_text, 2, 2, 1, 1)
        self.addFriend_text = QtWidgets.QLineEdit(self.centralwidget)
        self.addFriend_text.setText("")
        self.addFriend_text.setObjectName("addFriend_text")
        self.userDetails_grid.addWidget(self.addFriend_text, 9, 2, 1, 1)
        self.name_text = QtWidgets.QLabel(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.userDetails_grid.addWidget(self.name_text, 1, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.userDetails_grid.addWidget(self.listWidget, 14, 1, 1, 2)
        self.addFriend_label = QtWidgets.QLabel(self.centralwidget)
        self.addFriend_label.setObjectName("addFriend_label")
        self.userDetails_grid.addWidget(self.addFriend_label, 9, 1, 1, 1)
        self.motherBoard_text = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_text.setObjectName("motherBoard_text")
        self.userDetails_grid.addWidget(self.motherBoard_text, 5, 2, 1, 1)
        self.ip_ex_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_ex_label.setObjectName("ip_ex_label")
        self.userDetails_grid.addWidget(self.ip_ex_label, 3, 1, 1, 1)
        self.ip_in_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_in_label.setObjectName("ip_in_label")
        self.userDetails_grid.addWidget(self.ip_in_label, 4, 1, 1, 1)
        self.ip_ex_text = QtWidgets.QLabel(self.centralwidget)
        self.ip_ex_text.setObjectName("ip_ex_text")
        self.userDetails_grid.addWidget(self.ip_ex_text, 3, 2, 1, 1)
        self.ip_in_text = QtWidgets.QLabel(self.centralwidget)
        self.ip_in_text.setObjectName("ip_in_text")
        self.userDetails_grid.addWidget(self.ip_in_text, 4, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteFriend_button = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFriend_button.setObjectName("deleteFriend_button")
        self.horizontalLayout_2.addWidget(self.deleteFriend_button)
        self.addFriend_button = QtWidgets.QPushButton(self.centralwidget)
        self.addFriend_button.setObjectName("addFriend_button")
        self.horizontalLayout_2.addWidget(self.addFriend_button)
        self.userDetails_grid.addLayout(self.horizontalLayout_2, 10, 2, 1, 1)
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setObjectName("logout_button")
        self.userDetails_grid.addWidget(self.logout_button, 10, 1, 1, 1)
        self.horizontalLayout.addLayout(self.userDetails_grid)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "JBM"))
        self.motherBoard_label.setText(_translate("mainWindow", "Mother Board:"))
        self.lastName_label.setText(_translate("mainWindow", "Last Name:"))
        self.cpu_label.setText(_translate("mainWindow", "CPU:"))
        self.cpu_text.setText(_translate("mainWindow", "-----"))
        self.Jtag_text.setText(_translate("mainWindow", "-----"))
        self.name_label.setText(_translate("mainWindow", "Name:"))
        self.Jtag_label.setText(_translate("mainWindow", "ID:"))
        self.lastName_text.setText(_translate("mainWindow", "-----"))
        self.name_text.setText(_translate("mainWindow", "-----"))
        self.addFriend_label.setText(_translate("mainWindow", "Friend:"))
        self.motherBoard_text.setText(_translate("mainWindow", "-----"))
        self.ip_ex_label.setText(_translate("mainWindow", "IP(external):"))
        self.ip_in_label.setText(_translate("mainWindow", "IP(internal)"))
        self.ip_ex_text.setText(_translate("mainWindow", "-----"))
        self.ip_in_text.setText(_translate("mainWindow", "-----"))
        self.deleteFriend_button.setText(_translate("mainWindow", "Delete"))
        self.addFriend_button.setText(_translate("mainWindow", "ADD"))
        self.logout_button.setText(_translate("mainWindow", "Logout"))


    def __init__(self, user_id , user_pass , user_sudo):
        try:
            self.my_user = user.User(user_id, user_pass, user_sudo)
        except Exception as e:
            print(e)
            self.my_user = user.User.get_instance()
        """
        # remove all my friend
        for i in self.my_user.friends_list:
            self.my_user.remove_friend(i)
        """
        self.user_id = user_id
        self.user_password = user_pass
        self.user_sudo = user_sudo
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainPage = QtWidgets.QMainWindow()
        self.setupUi(self.mainPage)
        self.Jtag_text.setText(str(user_id))
        self.addFriend_button.clicked.connect(lambda: self.add_friend(self.addFriend_text.text()))
        self.listWidget.itemActivated.connect(self.itemActivated_event)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lastName_text.setText(self.my_user.last_name)
        self.name_text.setText(self.my_user.name)
        self.motherBoard_text.setText(self.my_user.get_my_motherboard())
        self.ip_ex_text.setText(self.my_user.get_my_external_ip().split()[0])
        self.ip_in_text.setText(self.my_user.get_my_internal_ip().split()[0])
        self.cpu_text.setText(self.my_user.get_my_cpu().strip().partition('\n')[0])
        self.deleteFriend_button.clicked.connect(self.remove_friend)
        self.logout_button.clicked.connect(self.logout)

        friend_status_thread = Thread(target=self.my_friend_status)
        friend_status_thread.start()

        msg_alarm_thread = Thread(target=self.msg_alarm)
        msg_alarm_thread.start()
        friend_status = self.my_user.get_friend_status()
        for name in friend_status.keys():
            print(friend_status[name])
            if friend_status[name]:
                item = QListWidgetItem('%s' % (name))
                self.listWidget.addItem(item)
                item.setBackground(QtGui.QColor('#ff944d'))
            else:
                item = QListWidgetItem('%s' % (name))
                self.listWidget.addItem(item)
                item.setBackground(QtGui.QColor('#ff0000'))

    def my_friend_status(self):
        while True:
            if len(self.my_user.connect_friend_queue) > 0:
                # change background of item for connected status
                data = self.my_user.connect_friend_queue.pop()["sender_id"]
                items = self.listWidget.findItems(str(data), QtCore.Qt.MatchExactly)
                if len(items) > 0:
                    for item in items:
                        item.setBackground(QtGui.QColor('#808000'))

            if len(self.my_user.disconnect_friend_queue) > 0:
                # change background of item for disconnect status
                data = self.my_user.disconnect_friend_queue.pop()["sender_id"]
                items = self.listWidget.findItems(str(data), QtCore.Qt.MatchExactly)
                if len(items) > 0:
                    for item in items:
                        item.setBackground(QtGui.QColor('#ff944d'))

            self.my_user.connect_status_waiter.acquire()
            self.my_user.connect_status_waiter.wait()
            self.my_user.connect_status_waiter.release()


        """
        here we need to get the user details by the id and put it in place.
        """

    def msg_alarm(self):
        while True:
            if len(self.my_user.sender_queue) > 0:
                data = self.my_user.sender_queue.pop()
                items = self.listWidget.findItems(str(data), QtCore.Qt.MatchExactly)
                if len(items) > 0:
                    for item in items:
                        blink_msg_thread = Thread(target=self.blink_msg, args=[item])
                        blink_msg_thread.start()
            self.my_user.my_queue_waiter.acquire()
            print("wating...")
            self.my_user.my_queue_waiter.wait()
            print("interupted")
            self.my_user.my_queue_waiter.release()

    def blink_msg(self, item):
        while True:
            print("orange")
            item.setBackground(QtGui.QColor('#ff944d'))
            sys.stdout.flush()
            time.sleep(3)
            print("black")
            item.setBackground(QtGui.QColor('#000000'))
            sys.stdout.flush()
            time.sleep(3)

    def logout(self):
        self.my_user.disconnect()
        os.system("pwd")
        login_screen_process = Process(target= os.system , args=("python3 login_ui.py" , ))
        login_screen_process.start()
        self.mainPage.hide()

    def open(self):
        self.mainPage.show()
        sys.exit(self.app.exec_())

    def remove_friend(self):
        """
        problem fixed!!!!
        :return:
        """
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.my_user.remove_friend(item.text())


    def add_friend(self, friend):
        my_user = user.User.get_instance()
        if my_user.add_friend(friend) and friend != "":
            friendList.append(friend)
            self.listWidget.addItem(friend)


    def open_chat(self,user_id):
         pass



    def get_friends(self):
        """

        :param user_id:
        :return:all the user friends

        for each friend - add the friend to the list with his detials.
         """
        return self.my_user.get_friends()




    def itemActivated_event(self,item):
        print(item.text())
        def open_chat_window(friend_id):
            chat_window_process = Process(target=os.system, args=("python3 chatWindow_ui.py " + str(self.user_id)+" "+str(self.user_password)+" "+str(self.user_sudo)+" "+str(friend_id),))
            chat_window_process.start()

        open_chat_window(item.text())


if __name__ == '__main__':
    #for the testing of the page only:
    try:
        userid = sys.argv[1]
        userpass = sys.argv[2]
        usersudo = sys.argv[3]
    except:
        if len(sys.argv) != 3:
            userid = "testUser2"
            userpass = "12345"
            usersudo = "1313"
        else:
            print("user details error!")



    window = Ui_mainWindow(userid, userpass, usersudo)
    window.open()

