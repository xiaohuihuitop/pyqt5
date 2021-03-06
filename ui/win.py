# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 750)
        MainWindow.setMinimumSize(QtCore.QSize(850, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1455, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 10, 641, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plainTextEdit_Receive = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_Receive.setGeometry(QtCore.QRect(0, 30, 641, 331))
        self.plainTextEdit_Receive.setReadOnly(True)
        self.plainTextEdit_Receive.setMaximumBlockCount(0)
        self.plainTextEdit_Receive.setObjectName("plainTextEdit_Receive")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 63, 14))
        self.label.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 390, 63, 14))
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_Send = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_Send.setGeometry(QtCore.QRect(0, 410, 641, 121))
        self.plainTextEdit_Send.setObjectName("plainTextEdit_Send")
        self.pushButton_send = QtWidgets.QPushButton(self.frame)
        self.pushButton_send.setGeometry(QtCore.QRect(539, 544, 85, 26))
        self.pushButton_send.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_clean = QtWidgets.QPushButton(self.frame)
        self.pushButton_clean.setGeometry(QtCore.QRect(539, 370, 85, 26))
        self.pushButton_clean.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.checkBox_Send = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Send.setGeometry(QtCore.QRect(460, 540, 79, 31))
        self.checkBox_Send.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.checkBox_Send.setObjectName("checkBox_Send")
        self.checkBox_Receive = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Receive.setGeometry(QtCore.QRect(460, 367, 79, 31))
        self.checkBox_Receive.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.checkBox_Receive.setObjectName("checkBox_Receive")
        self.lineEdit_Send_Timer = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Send_Timer.setGeometry(QtCore.QRect(30, 540, 71, 31))
        self.lineEdit_Send_Timer.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.lineEdit_Send_Timer.setObjectName("lineEdit_Send_Timer")
        self.checkBox_Send_Timer = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Send_Timer.setGeometry(QtCore.QRect(110, 550, 111, 16))
        self.checkBox_Send_Timer.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.checkBox_Send_Timer.setObjectName("checkBox_Send_Timer")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 600, 281, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox_com = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_com.setGeometry(QtCore.QRect(50, 20, 191, 31))
        self.comboBox_com.setStyleSheet("background-color: rgb(253, 237, 255);")
        self.comboBox_com.setPlaceholderText("")
        self.comboBox_com.setObjectName("comboBox_com")
        self.comboBox_com.addItem("")
        self.pushButton_open = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_open.setGeometry(QtCore.QRect(50, 60, 81, 51))
        self.pushButton_open.setStyleSheet("background-color: rgb(130, 255, 35);")
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_close = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_close.setGeometry(QtCore.QRect(160, 60, 81, 51))
        self.pushButton_close.setStyleSheet("background-color: rgb(255, 65, 48);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 21, 91))
        self.pushButton.setStyleSheet("background-color: rgb(248, 255, 121);")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 580, 211, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox_baud = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_baud.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.comboBox_baud.setStyleSheet("background-color: rgb(253, 237, 255);")
        self.comboBox_baud.setPlaceholderText("")
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_databit = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_databit.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.comboBox_databit.setStyleSheet("background-color: rgb(253, 237, 255);")
        self.comboBox_databit.setPlaceholderText("")
        self.comboBox_databit.setObjectName("comboBox_databit")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.comboBox_checkbit = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_checkbit.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.comboBox_checkbit.setStyleSheet("background-color: rgb(253, 237, 255);")
        self.comboBox_checkbit.setPlaceholderText("")
        self.comboBox_checkbit.setObjectName("comboBox_checkbit")
        self.comboBox_checkbit.addItem("")
        self.comboBox_stopbit = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_stopbit.setGeometry(QtCore.QRect(10, 130, 131, 31))
        self.comboBox_stopbit.setStyleSheet("background-color: rgb(253, 237, 255);")
        self.comboBox_stopbit.setPlaceholderText("")
        self.comboBox_stopbit.setObjectName("comboBox_stopbit")
        self.comboBox_stopbit.addItem("")
        self.comboBox_stopbit.addItem("")
        self.comboBox_stopbit.addItem("")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 63, 14))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(150, 60, 63, 14))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 63, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(150, 140, 63, 14))
        self.label_6.setObjectName("label_6")
        self.pw = GraphicsLayoutWidget(self.centralwidget)
        self.pw.setGeometry(QtCore.QRect(850, 40, 600, 551))
        self.pw.setObjectName("pw")
        self.pwstart = QtWidgets.QLineEdit(self.centralwidget)
        self.pwstart.setGeometry(QtCore.QRect(980, 620, 120, 30))
        self.pwstart.setObjectName("pwstart")
        self.pwend = QtWidgets.QLineEdit(self.centralwidget)
        self.pwend.setGeometry(QtCore.QRect(1220, 620, 120, 30))
        self.pwend.setObjectName("pwend")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1010, 600, 63, 14))
        self.label_7.setStyleSheet("color: rgb(133, 133, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1250, 600, 63, 14))
        self.label_8.setStyleSheet("color: rgb(205, 105, 255);")
        self.label_8.setObjectName("label_8")
        self.pw_clean = QtWidgets.QPushButton(self.centralwidget)
        self.pw_clean.setGeometry(QtCore.QRect(1360, 620, 85, 31))
        self.pw_clean.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pw_clean.setObjectName("pw_clean")
        self.checkBox_pw = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pw.setGeometry(QtCore.QRect(1130, 630, 79, 18))
        self.checkBox_pw.setObjectName("checkBox_pw")
        self.checkBox_pw_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pw_2.setGeometry(QtCore.QRect(1130, 670, 79, 18))
        self.checkBox_pw_2.setObjectName("checkBox_pw_2")
        self.pw_clean_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pw_clean_2.setGeometry(QtCore.QRect(1360, 660, 85, 31))
        self.pw_clean_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pw_clean_2.setObjectName("pw_clean_2")
        self.pwstart_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwstart_2.setGeometry(QtCore.QRect(980, 660, 120, 30))
        self.pwstart_2.setObjectName("pwstart_2")
        self.pwend_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwend_2.setGeometry(QtCore.QRect(1220, 660, 120, 30))
        self.pwend_2.setObjectName("pwend_2")
        self.pw_clean_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pw_clean_3.setGeometry(QtCore.QRect(1360, 700, 85, 31))
        self.pw_clean_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pw_clean_3.setObjectName("pw_clean_3")
        self.checkBox_pw_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pw_3.setGeometry(QtCore.QRect(1130, 710, 79, 18))
        self.checkBox_pw_3.setObjectName("checkBox_pw_3")
        self.pwstart_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwstart_3.setGeometry(QtCore.QRect(980, 700, 120, 30))
        self.pwstart_3.setObjectName("pwstart_3")
        self.pwend_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwend_3.setGeometry(QtCore.QRect(1220, 700, 120, 30))
        self.pwend_3.setObjectName("pwend_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "接收区"))
        self.label_2.setText(_translate("MainWindow", "发送区"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
        self.pushButton_clean.setText(_translate("MainWindow", "清空"))
        self.checkBox_Send.setText(_translate("MainWindow", "HEX"))
        self.checkBox_Receive.setText(_translate("MainWindow", "HEX"))
        self.lineEdit_Send_Timer.setText(_translate("MainWindow", "100"))
        self.checkBox_Send_Timer.setText(_translate("MainWindow", "定时发送(ms)"))
        self.comboBox_com.setCurrentText(_translate("MainWindow", "COMX"))
        self.comboBox_com.setItemText(0, _translate("MainWindow", "COMX"))
        self.pushButton_open.setText(_translate("MainWindow", "打开"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        self.pushButton.setText(_translate("MainWindow", "刷\n"
"\n"
"新"))
        self.comboBox_baud.setCurrentText(_translate("MainWindow", "921600"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "921600"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "256000"))
        self.comboBox_baud.setItemText(2, _translate("MainWindow", "128000"))
        self.comboBox_baud.setItemText(3, _translate("MainWindow", "115200"))
        self.comboBox_baud.setItemText(4, _translate("MainWindow", "57600"))
        self.comboBox_baud.setItemText(5, _translate("MainWindow", "19200"))
        self.comboBox_baud.setItemText(6, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(7, _translate("MainWindow", "4800"))
        self.comboBox_databit.setCurrentText(_translate("MainWindow", "8"))
        self.comboBox_databit.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_databit.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox_databit.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox_databit.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_checkbit.setCurrentText(_translate("MainWindow", "NONE"))
        self.comboBox_checkbit.setItemText(0, _translate("MainWindow", "NONE"))
        self.comboBox_stopbit.setCurrentText(_translate("MainWindow", "1"))
        self.comboBox_stopbit.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stopbit.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_stopbit.setItemText(2, _translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "波特率"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        self.label_5.setText(_translate("MainWindow", "校验位"))
        self.label_6.setText(_translate("MainWindow", "停止位"))
        self.label_7.setText(_translate("MainWindow", "数据头"))
        self.label_8.setText(_translate("MainWindow", "数据尾"))
        self.pw_clean.setText(_translate("MainWindow", "清除图像"))
        self.checkBox_pw.setText(_translate("MainWindow", "绘制"))
        self.checkBox_pw_2.setText(_translate("MainWindow", "绘制"))
        self.pw_clean_2.setText(_translate("MainWindow", "清除图像"))
        self.pw_clean_3.setText(_translate("MainWindow", "清除图像"))
        self.checkBox_pw_3.setText(_translate("MainWindow", "绘制"))
from pyqtgraph import GraphicsLayoutWidget
import ui.pic.pic_rc
