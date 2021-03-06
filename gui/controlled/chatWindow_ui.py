import sys
import random

from encryption.DES.driver import encrypt, decrypt

sys.path.append("../..")
# import os
import datetime
from threading import Thread
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QListWidgetItem, QMessageBox
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
from client import user
import COLORS
import os


"""popUP class
class AskForControlPopup(QWidget):
    def message_box(self, friend_name):
        resp = QMessageBox.question(self, 'Approve control', 'Do you approve to ' + friend_name + " to control yours computer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resp == QMessageBox.Yes:
            return True
        else:
            return False
"""


class Ui_friend_msgBox(object):
    def setupUi(self, friend_msgBox):
        friend_msgBox.setObjectName("friend_msgBox")
        friend_msgBox.resize(1200, 700)
        font = QtGui.QFont()
        font.setKerning(True)
        friend_msgBox.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        friend_msgBox.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(friend_msgBox)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chat_text = QtWidgets.QListWidget(self.centralwidget)
        self.chat_text.setAutoScroll(True)
        self.chat_text.setObjectName("chat_text")
        self.gridLayout_2.addWidget(self.chat_text, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.empty_label2 = QtWidgets.QLabel(self.centralwidget)
        self.empty_label2.setText("")
        self.empty_label2.setObjectName("empty_label2")
        self.gridLayout_3.addWidget(self.empty_label2, 0, 1, 1, 1)
        self.message_button = QtWidgets.QPushButton(self.centralwidget)
        self.message_button.setObjectName("message_button")
        self.gridLayout_3.addWidget(self.message_button, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 2, 1, 1)
        self.ssh_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ssh_text.setObjectName("ssh_text")
        self.gridLayout_2.addWidget(self.ssh_text, 3, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 3, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ssh_button = QtWidgets.QPushButton(self.centralwidget)
        self.ssh_button.setObjectName("ssh_button")
        self.gridLayout_4.addWidget(self.ssh_button, 0, 0, 1, 1)
        self.empty_label = QtWidgets.QLabel(self.centralwidget)
        self.empty_label.setText("")
        self.empty_label.setObjectName("empty_label")
        self.gridLayout_4.addWidget(self.empty_label, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.motherBoard_text = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_text.setObjectName("motherBoard_text")
        self.gridLayout.addWidget(self.motherBoard_text, 6, 1, 1, 1)
        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.allow_no_button = QtWidgets.QPushButton(self.centralwidget)
        self.allow_no_button.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 148, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 148, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.allow_no_button.setPalette(palette)
        self.allow_no_button.setObjectName("allow_no_button")
        self.horizontalLayout_2.addWidget(self.allow_no_button)
        self.allow_yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.allow_yes_button.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 231, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 192, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 103, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 204, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 231, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 192, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 103, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 204, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 231, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 192, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 103, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 77, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.allow_yes_button.setPalette(palette)
        self.allow_yes_button.setCheckable(False)
        self.allow_yes_button.setAutoDefault(False)
        self.allow_yes_button.setDefault(False)
        self.allow_yes_button.setFlat(False)
        self.allow_yes_button.setObjectName("allow_yes_button")
        self.horizontalLayout_2.addWidget(self.allow_yes_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 10, 1, 1, 1)
        self.ip_in_text = QtWidgets.QLabel(self.centralwidget)
        self.ip_in_text.setObjectName("ip_in_text")
        self.gridLayout.addWidget(self.ip_in_text, 4, 1, 1, 1)
        self.name_text = QtWidgets.QLabel(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.gridLayout.addWidget(self.name_text, 1, 1, 1, 1)
        self.ip_in_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_in_label.setObjectName("ip_in_label")
        self.gridLayout.addWidget(self.ip_in_label, 4, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(friend_msgBox)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.gridLayout.addWidget(self.radioButton_2, 12, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.allow_control_label = QtWidgets.QLabel(self.centralwidget)
        self.allow_control_label.setObjectName("allow_control_label")
        self.gridLayout.addWidget(self.allow_control_label, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.centralwidget)
        self.lastName_label.setObjectName("lastName_label")
        self.gridLayout.addWidget(self.lastName_label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.control_text = QtWidgets.QLabel(self.centralwidget)
        self.control_text.setObjectName("control_text")
        self.gridLayout.addWidget(self.control_text, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.ip_text = QtWidgets.QLabel(self.centralwidget)
        self.ip_text.setObjectName("ip_text")
        self.gridLayout.addWidget(self.ip_text, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 13, 0, 1, 1)
        self.control_label = QtWidgets.QLabel(self.centralwidget)
        self.control_label.setObjectName("control_label")
        self.gridLayout.addWidget(self.control_label, 9, 0, 1, 1)
        self.motherBoard_label = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_label.setObjectName("motherBoard_label")
        self.gridLayout.addWidget(self.motherBoard_label, 6, 0, 1, 1)
        self.show_his_ssh_commands_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.show_his_ssh_commands_rb.setObjectName("show_his_ssh_commands_rb")
        self.buttonGroup_2.addButton(self.show_his_ssh_commands_rb)
        self.gridLayout.addWidget(self.show_his_ssh_commands_rb, 12, 1, 1, 1)
        self.ask_for_control_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ask_for_control_button.setObjectName("ask_for_control_button")
        self.gridLayout.addWidget(self.ask_for_control_button, 11, 0, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_2, 11, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.lastName_text = QtWidgets.QLabel(self.centralwidget)
        self.lastName_text.setObjectName("lastName_text")
        self.gridLayout.addWidget(self.lastName_text, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 2, 1, 1)
        self.message_text = QtWidgets.QLineEdit(self.centralwidget)
        self.message_text.setObjectName("message_text")
        self.gridLayout_2.addWidget(self.message_text, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        friend_msgBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(friend_msgBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 22))
        self.menubar.setObjectName("menubar")
        friend_msgBox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(friend_msgBox)
        self.statusbar.setObjectName("statusbar")
        friend_msgBox.setStatusBar(self.statusbar)

        self.retranslateUi(friend_msgBox)
        QtCore.QMetaObject.connectSlotsByName(friend_msgBox)
        friend_msgBox.setTabOrder(self.ask_for_control_button, self.commandLinkButton_2)
        friend_msgBox.setTabOrder(self.commandLinkButton_2, self.chat_text)

    def retranslateUi(self, friend_msgBox):
        _translate = QtCore.QCoreApplication.translate
        friend_msgBox.setWindowTitle(_translate("friend_msgBox", "chat with"))
        self.message_button.setText(_translate("friend_msgBox", "Send Message"))
        self.ssh_button.setText(_translate("friend_msgBox", "Send SSH Command"))
        self.motherBoard_text.setText(_translate("friend_msgBox", "-----"))
        self.ip_label.setText(_translate("friend_msgBox", "ip(external):"))
        self.allow_no_button.setText(_translate("friend_msgBox", "NO"))
        self.allow_yes_button.setText(_translate("friend_msgBox", "Yes"))
        self.ip_in_text.setText(_translate("friend_msgBox", "-----"))
        self.name_text.setText(_translate("friend_msgBox", "-----"))
        self.ip_in_label.setText(_translate("friend_msgBox", "ip(internal):"))
        self.radioButton_2.setText(_translate("friend_msgBox", "don\'t show ssh dialog"))
        self.label.setText(_translate("friend_msgBox", "CPU:"))
        self.allow_control_label.setText(_translate("friend_msgBox", "Allow Control:"))
        self.label_2.setText(_translate("friend_msgBox", "-----"))
        self.lastName_label.setText(_translate("friend_msgBox", "Last Name:"))
        self.label_3.setText(_translate("friend_msgBox", "SSH Details:"))
        self.control_text.setText(_translate("friend_msgBox", "Not Alowed"))
        self.ip_text.setText(_translate("friend_msgBox", "-----"))
        self.control_label.setText(_translate("friend_msgBox", "Control:"))
        self.motherBoard_label.setText(_translate("friend_msgBox", "Mother Board:"))
        self.show_his_ssh_commands_rb.setText(_translate("friend_msgBox", "show ssh dialog"))
        self.ask_for_control_button.setText(_translate("friend_msgBox", "Ask for Control"))
        self.commandLinkButton_2.setText(_translate("friend_msgBox", "Disable his control"))
        self.name_label.setText(_translate("friend_msgBox", "Name:"))
        self.label_13.setText(_translate("friend_msgBox", "Friend Details:"))
        self.lastName_text.setText(_translate("friend_msgBox", "-----"))


    def __init__(self, user_id, user_pass, user_sudo, friend_id):
        # from client import user
        # self.get_ask_for_control = False
        # self.main_wake_up = Condition()
        self.user_id = user_id
        self.user_password = user_pass
        self.user_sudo = user_sudo
        try:
            self.my_user = my_user = user.User(self.user_id, self.user_password, self.user_sudo)
        except Exception as e:
            #print(e)
            self.my_user = my_user = user.User.get_instance()
        self.my_user.swap_keys(friend_id)
        self.friend_id = friend_id
        self.first_msg = True
        self.app = QtWidgets.QApplication(sys.argv)
        self.friend_msgBox = QtWidgets.QMainWindow()
        # override a contain object method
        self.friend_msgBox.closeEvent = self.closeEvent
        self.setupUi(self.friend_msgBox)

        self.message_text.returnPressed.connect(self.message_button.animateClick)
        self.ssh_text.returnPressed.connect(self.ssh_button.animateClick)
        self.motherBoard_text.setText(my_user.get_friend_motherboard(friend_id))
        self.name_text.setText(my_user.get_friend_name(friend_id))
        self.ip_text.setText(my_user.get_friend_external_ip(friend_id))
        self.ip_in_text.setText(my_user.get_friend_internal_ip(friend_id))
        self.label_2.setText(my_user.get_friend_cpu(friend_id))
        self.lastName_text.setText(my_user.get_friend_last_name(friend_id))
        self.chat_text.scrollToBottom()

        # define buttons click events
        self.message_button.clicked.connect(self.send_msg)
        self.allow_yes_button.clicked.connect(self.approve_control)
        self.allow_no_button.clicked.connect(self.reject_ask_for_control)
        self.ask_for_control_button.clicked.connect(self.ask_for_control)
        self.ssh_button.clicked.connect(self.send_ssh_msg)
        self.commandLinkButton_2.clicked.connect(self.disable_control)
        self.chat_text.scrollToBottom()
        self.show_his_ssh_commands_rb.toggled.connect(self.show_his_ssh_commands)
        self.radioButton_2.toggled.connect(self.dont_show_his_ssh_commands)
        self.show_his_ssh_commands_rb.toggle()

        def get_messages_process():
            #from multiprocessing.pool import ThreadPool
            my_thread_for_simple_msgs = Thread(target=listen_msg)
            my_thread_for_simple_msgs.daemon = True
            try:
                my_thread_for_simple_msgs.start()
            except:
                pass
                # print("stop wating for new messages")
            my_thread_for_ssh_msgs = Thread(target=listen_to_ssh_msg)
            my_thread_for_ssh_msgs.daemon = True
            my_thread_for_ssh_msgs.start()

        def listen_msg():
            while True:
                if len(my_user.my_queue) > 0:
                    data = self.my_user.my_queue.pop()
                    #print(self.my_user.id + "  got message from :" + data['sender_id'])
                    if self.friend_id == data['sender_id']:
                        if str(data['text']).startswith('DH-protocol!@#$'):
                            keys= data['text'].split()
                            p=int(keys[1])
                            alpha=int(keys[2])
                            friend_public_key=int(keys[3])
                            my_private_key = random.randrange(1, p)
                            my_user.my_private_key=my_private_key
                            my_user.p=p
                            my_user.alpha=alpha
                            my_public_key = ((alpha) ** my_private_key) % p
                            my_user.chat_key = (friend_public_key**my_private_key)%p
                            print(my_user.chat_key)
                            self.send_key("DH-protocol_getting_pub_key!@#$ " + str(my_public_key) + " "+str(p) + " " + str(alpha))
                        elif str(data['text']).startswith('DH-protocol_getting_pub_key!@#$'):
                            keys= data['text'].split()
                            friend_public_key = int(keys[1])
                            my_user.chat_key = (friend_public_key ** int(my_user.my_private_key)) % my_user.p
                            print(my_user.chat_key)
                        else:
                            decrypt_msg=decrypt(data['text'],self.my_user.chat_key)
                            while decrypt_msg[-1:]=="0":
                                decrypt_msg=decrypt_msg[:-1]
                            item = QListWidgetItem('%s' % (data['sender_name'] + " > " + decrypt_msg))
                            item.setBackground(QtGui.QColor(COLORS.light_blue))
                            self.chat_text.addItem(item)
                            self.chat_text.scrollToBottom()
                else:
                    self.my_user.my_queue_waiter.acquire()
                    # print("wating for new messages..")
                    self.my_user.my_queue_waiter.wait()
                    # print("new message arrived!")
                    self.my_user.my_queue_waiter.release()

        def listen_to_ssh_msg():
            while True:
                print("ssh message")
                if len(my_user.ssh_results_command_queue) > 0:
                    data = self.my_user.ssh_results_command_queue.pop()
                    print(data['ssh_cmd'])
                    # print(self.my_user.id + "  got message from :" + data['sender_id'])
                    if self.friend_id == data['sender_id']:
                        item = QListWidgetItem('%s' % (data['sender_id'] + " > " + data['ssh_cmd']))
                        # item.setForeground(COLORS.white)
                        item.setBackground(QtGui.QColor(COLORS.red))
                        self.chat_text.addItem(item)
                        self.chat_text.scrollToBottom()


                else:
                    self.my_user.ssh_results_command_queue_waiter.acquire()
                    # print("wating for new SSH command...")
                    self.my_user.ssh_results_command_queue_waiter.wait()
                    # print("new SSH command arrived!")
                    self.my_user.ssh_results_command_queue_waiter.release()

        def get_control_req_process():
            my_thread = Thread(target=listen_to_control_req)
            my_thread.daemon = True
            my_thread.start()

        # class represent popup
        #self.popup = AskForControlPopup()

        def listen_to_control_req():
            while True:
                # print("listen to req ask")
                set_of_req = my_user.approve_control_requests
                if len(set_of_req) > 0 and friend_id in set_of_req:
                    # print("get req ask")
                    self.allow_yes_button.setCheckable(True)
                    self.allow_yes_button.setEnabled(True)
                    self.allow_no_button.setCheckable(True)
                    self.allow_no_button.setEnabled(True)
                    """for popup instead buttons
                    self.get_ask_for_control = True

                    ans = self.popup.message_box(friend_id)
                    if ans:
                        print("yes")
                        my_user.approve_control(friend_id, True)
                        self.control_text.setText("Allowed")
                    elif not ans:
                        my_user.approve_control(friend_id, False)
                        print("no")
                    """
                    """ to delete
                    self.main_wake_up.acquire()
                    self.main_wake_up.notify()
                    self.main_wake_up.release()
                    """
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
    def show_his_ssh_commands(self):
        self.my_user.show_ssh_res = True

    def dont_show_his_ssh_commands(self):
        self.my_user.show_ssh_res = False

    def approve_control(self):
        self.my_user.approve_control(self.friend_id, True)
        self.allow_yes_button.setCheckable(False)
        self.allow_yes_button.setEnabled(False)
        self.allow_no_button.setCheckable(False)
        self.allow_no_button.setEnabled(False)
        self.control_text.setText("Allowed")

    def reject_ask_for_control(self):
        self.my_user.approve_control(self.friend_id, False)
        self.allow_yes_button.setCheckable(False)
        self.allow_yes_button.setEnabled(False)
        self.allow_no_button.setCheckable(False)
        self.allow_no_button.setEnabled(False)

    def ask_for_control(self):
        self.my_user.ask_for_control(self.friend_id)
        encrypted_msg = encrypt("can i control yours computer? (press 'yes' or 'no' button)", self.my_user.chat_key)
        t = Thread(target=self.my_user.send_message, args=(self.friend_id, encrypted_msg))
        t.daemon = True
        t.start()

    def disable_control(self):
        self.my_user.remove_control(self.friend_id)
        # print(self.my_user.approved_control)
        self.get_ask_for_control = False
        self.control_text.setText("Not Allowed")

    def send_msg(self):
        msg_txt = self.message_text.text()
        encrypt_msg= encrypt(msg_txt,self.my_user.chat_key)
        # print("my text is " + msg_txt)
        self.chat_text.scrollToBottom()
        if msg_txt != '':
            '''
            # send date at the start of conversation
            if self.first_msg:
                date = datetime.date.today().strftime("%B %d, %Y")
                item = QListWidgetItem('%s' % (date))
                self.chat_text.addItem(item)
                item.setBackground(QtGui.QColor('#fad000'))
                date= encrypt(date,self.my_user.chat_key)
                t = Thread(target=self.my_user.send_message, args=(self.friend_id, date))
                t.daemon = True
                # self.my_user.send_message(self.friend_id, msg_txt)
                t.start()
                self.first_msg = False
                time.sleep(0.8)
            '''
            item = QListWidgetItem('%s' % (self.my_user.name + " > " + msg_txt))
            self.chat_text.addItem(item)
            item.setBackground(QtGui.QColor('#ff944d'))
            self.message_text.setText("")
            t = Thread(target=self.my_user.send_message, args=(self.friend_id , encrypt_msg))
            t.daemon = True
            #self.my_user.send_message(self.friend_id, msg_txt)
            t.start()
            self.chat_text.scrollToBottom()

    def send_key(self, text=""):
        if text == "":
            msg_txt = self.message_text.text()
        else:
            msg_txt = str(text)
        # print("my text is " + msg_txt)
        self.chat_text.scrollToBottom()
        if msg_txt != '':
            '''
            # send date at the start of conversation
            if self.first_msg:
                date = datetime.date.today().strftime("%B %d, %Y")
                item = QListWidgetItem('%s' % (date))
                self.chat_text.addItem(item)
                item.setBackground(QtGui.QColor('#fad000'))
                t = Thread(target=self.my_user.send_message, args=(self.friend_id, date))
                t.daemon = True
                # self.my_user.send_message(self.friend_id, msg_txt)
                t.start()
                self.first_msg = False
                time.sleep(0.8)
            '''
            item = QListWidgetItem('%s' % (self.my_user.name + " > " + msg_txt))
            self.chat_text.addItem(item)
            item.setBackground(QtGui.QColor('#ff944d'))
            self.message_text.setText("")
            t = Thread(target=self.my_user.send_message, args=(self.friend_id, msg_txt))
            t.daemon = True
            # self.my_user.send_message(self.friend_id, msg_txt)
            t.start()
            self.chat_text.scrollToBottom()

    def closeEvent(self, *args):
        self.my_user.disconnect_from_chat()
        try:
            path = os.path.expanduser('~')
            path = path + '/url.txt'
            os.remove(path)
        except:
            pass
        # print("window closed")

    def send_ssh_msg(self):
        msg_txt = self.ssh_text.text()
        #print("my text is " + msg_txt)
        self.chat_text.scrollToBottom()
        if msg_txt != '':
            item = QListWidgetItem('%s' % (self.my_user.name + "shh req >> " + msg_txt))
            item.setForeground(QtGui.QColor(COLORS.white))
            item.setBackground(QtGui.QColor(COLORS.black))
            self.chat_text.addItem(item)
            self.ssh_text.setText("")
            t = Thread(target=self.my_user.send_ssh_message, args=(self.friend_id, msg_txt))
            t.daemon = True
            t.start()
            #self.my_user.send_ssh_message(self.friend_id, msg_txt)
            self.chat_text.scrollToBottom()



    def open(self):
        self.friend_msgBox.show()
        sys.exit(self.app.exec_())



if __name__ == '__main__':
    # for the testing of the page only:
    # x = Ui_mainWindow(sys.argv[1])s
    try:
        
        default_id1 = 'mmttdd'
        default_id2 = 'tomdamri'
        default_pas = '12345'
        default_sudo = '123'

        try:
            # print(f"loading {sys.argv[4]} details.. that can take a moment..")
            x = Ui_friend_msgBox(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        except:
            # print("error accured with input, or U running a test")
            x = Ui_friend_msgBox(default_id1, default_pas, default_sudo, default_id2)

        x.open()
    except Exception as e:
        print(e)
        print('Error has accurred or window got closed.')
    print("main thread closed")
    # print(x.messages)

    
"""
    while True:
        print("main wait - req ask")
        if x.get_ask_for_control:
            print("main in popup")
            ap = App()
            ans = ap.message_box(x.friend_id)
            if ans:
                print("yes")
                x.my_user.approve_control(x.friend_id, True)
                x.control_text.setText("Allowed")
            elif not ans:
                x.my_user.approve_control(x.friend_id, False)
                print("no")
        print("main wait")
        x.main_wake_up.acquire()
        x.main_wake_up.wait()
        x.main_wake_up.release()
        print("main wake up")
"""