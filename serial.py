from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QCheckBox
from PyQt5.QtCore import QSettings, QIODevice, QTimer  # 配置文件使用
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo  # 使用qt提供的串口工具 serial 这个模块是python的
from PyQt5.QtGui import QIntValidator
from ui.win import Ui_MainWindow
import datetime
import binascii
import pyqtgraph as pg
import pandas as pd
import numpy as np
import re

pwData = ''
pwData2 = ''
pwData3 = ''
pwDataarr = [0]
pwDataarr2 = [0]
pwDataarr3 = [0]
ptr1 = 0


# def print(*args, **kwargs):
#     pass

class GetWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GetWin, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("小灰灰串口工具")

        # 配置文件
        self.settings = QSettings("config.ini", QSettings.IniFormat)

        # 获取
        # self.com = self.settings.value("SETUP/COM_VALUE")
        self.baud = self.settings.value("SETUP/BAUD_VALUE")
        self.databit = self.settings.value("SETUP/DATABIT_VALUE")
        self.checkbit = self.settings.value("SETUP/CHECKBIT_VALUE")
        self.stopbit = self.settings.value("SETUP/STOPBIT_VALUE")
        # 设置
        if self.baud is None:
            self.baud = 9600
            self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存
        if self.databit is None:
            self.databit = 8
            self.settings.setValue("SETUP/DATABIT_VALUE", self.databit)  # 保存
        if self.checkbit is None:
            self.checkbit = "NONE"
            self.settings.setValue("SETUP/CHECKBIT_VALUE", self.checkbit)  # 保存
        if self.stopbit is None:
            self.stopbit = 1
            self.settings.setValue("SETUP/STOPBIT_VALUE", self.stopbit)  # 保存

        # 赋值
        self.comboBox_baud.setCurrentText(str(self.baud))
        self.comboBox_databit.setCurrentText(str(self.databit))
        self.comboBox_checkbit.setCurrentText(str(self.checkbit))
        self.comboBox_stopbit.setCurrentText(str(self.stopbit))

        # 串口类
        self.com = QSerialPort()

        # 时间类 定时发送使用
        self.timer_receive = QTimer()
        self.timer_send = QTimer()

        self.timer_receive.timeout.connect(self.com_receive_cb)
        self.timer_send.timeout.connect(self.button_send_cb)

        # 信号槽
        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.comboBox_databit.currentIndexChanged.connect(self.combox_databit_cb)
        self.comboBox_checkbit.currentIndexChanged.connect(self.combox_checkbit_cb)
        self.comboBox_stopbit.currentIndexChanged.connect(self.combox_stopbit_cb)

        self.checkBox_Send.stateChanged.connect(self.checkbox_send_cb)  # 发送 HEX
        self.checkBox_Send_Timer.stateChanged.connect(self.checkbox_timer_cb)

        self.pushButton.clicked.connect(self.button_refresh_cb)  # 刷新端口
        self.pushButton_open.clicked.connect(self.button_open_cb)  # 打开端口
        self.pushButton_close.clicked.connect(self.button_close_cb)  # 关闭端口

        self.pushButton_send.clicked.connect(self.button_send_cb)  # 发送据数
        # self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 这里连接无效 需要在打开com口后再链接
        self.pushButton_clean.clicked.connect(self.button_clean_cb)  # 清除按钮

        # 自动滚屏
        self.plainTextEdit_Receive.textChanged.connect(self.text_scroll)

        # 数据图形化
        self.plainTextEdit_Receive.textChanged.connect(self.pw_update)  # 每次改变数据 会更新一次全局 pwData
        self.pw_clean.clicked.connect(self.pw_cleandata)  ## 清除图像
        self.pw_clean_2.clicked.connect(self.pw_cleandata2)  ## 清除图像
        self.pw_clean_3.clicked.connect(self.pw_cleandata3)  ## 清除图像

        # 初始操作
        self.button_refresh_cb()
        self.pushButton_close.setDisabled(True)
        self.lineEdit_Send_Timer.setValidator(QIntValidator(0, 99999))  # 设置定时发送数据范围

        # graph 设置
        self.pw.setWindowTitle("小灰灰Main")
        self.pw1 = self.pw.addPlot()
        self.pw1.setTitle("小灰灰", color='00ffff', size='12pt')
        self.pw1.setLabel("left", "数据")
        self.pw1.setLabel("bottom", "时间")
        # self.pw1.setBackground('w')  # 背景颜色

        self.pw1.showGrid(x=True, y=True)  # 网格
        self.pw1.setClipToView(True)

        # 鼠标移动获取数据
        self.pw1.plot().scene().sigMouseClicked.connect(self.mouseClicked)  # 绑定槽

        # 显示线

        # self.pw2 = self.pw.add
        # self.timer_pw = QTimer(self)  # 设置定时器
        # self.timer_pw.timeout.connect(self.pw_update)  # 链接
        # self.timer_pw.start(50)  # 1秒钟一次

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()
        self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存

    def combox_databit_cb(self):
        self.databit = self.comboBox_databit.currentText()
        self.settings.setValue("SETUP/DATABIT_VALUE", self.databit)  # 保存

    def combox_checkbit_cb(self):
        self.checkbit = self.comboBox_checkbit.currentText()
        self.settings.setValue("SETUP/CHECKBIT_VALUE", self.checkbit)  # 保存

    def combox_stopbit_cb(self):
        self.stopbit = self.comboBox_stopbit.currentText()
        self.settings.setValue("SETUP/STOPBIT_VALUE", self.stopbit)  # 保存

    def button_refresh_cb(self):
        com_list = QSerialPortInfo.availablePorts()  # 获取所有的端口信息
        for com in com_list:
            print(com.portName())  # 返回串口号，如COM1
            print(com.description())  # 返回设备硬件描述 如USB-SERIAL CH340
            print(com.productIdentifier())  # 返回设备编号 如29987
            print(
                com.standardBaudRates())  # 返回设备的支持波特率列表 如[110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200, 128000, 256000]
            if com.portName() is not None:  # 判断是否为空
                pass
                if self.comboBox_com.findText(com.portName() + " # " + com.description()) < 0:  # 判断com口是否重复
                    print(self.comboBox_com.findText(com.portName()))  # 测试
                    self.comboBox_com.addItem(com.portName() + " # " + com.description())  # 添加item

    def button_open_cb(self):
        print("open")
        port = self.comboBox_com.currentText()[:5]  # 获取 COM名字
        print(port)
        self.com = QSerialPort()
        self.com.setPortName(port)  # 使用名字 绑定COM口
        if self.com.open(QSerialPort.ReadWrite) == False:  # QSerialPort  QIODevice  打开端口
            print("open err")
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return

        if self.com.isOpen():
            print("is open")
            print(self.baud)
            self.com.setBaudRate(int(self.baud))  # 波特率
            # self.com.setDataBits(self.com.Data8)  # 8
            self.com.setDataBits(int(self.databit))
            if self.checkbit == "NONE":
                self.com.setParity(self.com.NoParity)  # n
            else:
                self.com.setParity(self.com.NoParity)  # n
            # self.com.setStopBits(self.com.OneStop)  # 1
            self.com.setStopBits(int(self.stopbit))
            self.com.setFlowControl(self.com.NoFlowControl)
            print("set over")
            print(self.com.baudRate())  # 验证波特率

            # self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 需要打开串口后再调用 此处有效
            self.timer_receive.start(100)  # 接收数据 定时
            self.comboBox_com.setDisabled(True)
            # self.comboBox_baud.setDisabled(True)
            # self.comboBox_databit.setDisabled(True)
            # self.comboBox_checkbitbit.setDisabled(True)
            # self.comboBox_stopbitbit.setDisabled(True)

            self.pushButton_open.setDisabled(True)
            self.pushButton_close.setDisabled(False)
        pass

    def button_close_cb(self):
        print("close")
        port = self.comboBox_com.currentText()[:5]
        print(port)
        self.com = QSerialPort()
        self.com.setPortName(port)
        self.com.close()

        self.comboBox_com.setDisabled(False)
        # self.comboBox_baud.setDisabled(False)
        # self.comboBox_databit.setDisabled(False)
        # self.comboBox_checkbitbit.setDisabled(False)
        # self.comboBox_stopbitbit.setDisabled(False)

        self.pushButton_open.setDisabled(False)
        self.pushButton_close.setDisabled(True)
        pass

    def button_send_cb(self):
        global pwData  # 测试使用
        alist = []
        print("send")
        time_stamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
        print(time_stamp)

        if self.checkBox_Send.isChecked():
            txDataHex = self.plainTextEdit_Send.toPlainText()
            print(txDataHex)
            txData = txDataHex.replace(" ", "")  # 取消空格 准备转16进制
            # if len(txData) % 2 == 1:  # 去除独立数据
            #     txData = txData[0:len(txData) - 1]
            #     print("------",txData)

            for i in range(0, len(txData), 2):
                temp = txData[i:i + 2]
                try:  # 判断
                    temp_hex = int(temp, 16)
                    print(temp_hex)
                    alist.append(temp)
                except:
                    QMessageBox.critical(self, '严重错误', '含有非16')
                    if self.checkBox_Send_Timer.isChecked():
                        self.checkBox_Send_Timer.setCheckState(0)
                    return

            txData = " ".join(alist)
            print(txData)
            self.com.write(txData.encode('UTF-8'))  # 编码为bytes再发送

            # 处理显示部分
            txDataHex = txDataHex.replace(" ", "")  # 取消空格
            print(txDataHex)

            alist = []
            #  将字符串 分割 加入列表
            for i in range(0, len(txDataHex), 2):
                alist.append(txDataHex[i:i + 2])

            txDataHex = " ".join(alist)  # 使用 ” “ 空格 将列表中的数据连接 就变成了 带空格的16进制数据
            print(txDataHex)

            self.plainTextEdit_Receive.insertPlainText(
                time_stamp + "发->" + txDataHex + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
        else:
            txData = self.plainTextEdit_Send.toPlainText()
            pwData = txData
            print(txData)
            print(txData.encode('UTF-8'))
            self.com.write(txData.encode('UTF-8'))
            self.plainTextEdit_Receive.insertPlainText(
                time_stamp + "发->" + txData + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1

    def com_receive_cb(self):
        global pwData  # 从串口中得到的准备显示的数据
        # print("receive_cb")
        rxData = bytes(self.com.readAll())
        if len(rxData) > 0:
            time_stamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
            if not self.checkBox_Receive.isChecked():
                try:
                    # print(rxData.decode('ascii'))  ## 测试
                    pwData = rxData.decode('utf-8') + "\n"
                    self.plainTextEdit_Receive.insertPlainText(time_stamp + "收->")
                    self.plainTextEdit_Receive.insertPlainText(
                        rxData.decode('utf-8') + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
                except:
                    pwData = rxData.decode('ISO-8859-1') + "\n"
                    self.plainTextEdit_Receive.insertPlainText(
                        rxData.decode('ISO-8859-1') + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
            else:
                try:
                    self.plainTextEdit_Receive.insertPlainText(time_stamp + "收->")
                    rxDataHex = binascii.hexlify(rxData, " ").decode("utf-8")  # 转为 utf8字符串
                    self.plainTextEdit_Receive.insertPlainText(rxDataHex + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
                except:
                    rxDataHex = binascii.hexlify(rxData, " ").decode("ISO-8859-1")  # 转为 utf8字符串
                    self.plainTextEdit_Receive.insertPlainText(rxDataHex + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
                pass

    def button_clean_cb(self):
        print("clean")
        self.plainTextEdit_Receive.clear()

    def text_scroll(self):
        self.plainTextEdit_Receive.verticalScrollBar().setValue(
            self.plainTextEdit_Receive.verticalScrollBar().maximum())

    def checkbox_send_cb(self):
        if self.checkBox_Send.isChecked():  # 当前需要显示hex
            #  将 发送框中的数据转为 16进制
            print("utf8 to 16")
            alist = []
            txData = self.plainTextEdit_Send.toPlainText().encode('UTF-8')  # 获取到数据 并转为 bytes
            print(txData)

            # txDataHex = binascii.b2a_hex(txData).decode("utf-8") # 转为16进制 字符串 并解码为 utf8
            #
            # #  将字符串 分割 加入列表
            # for i in range(0, len(txDataHex), 2):
            #     alist.append(txDataHex[i:i+2])
            #
            # txDataHex = " ".join(alist)  # 使用 ” “ 空格 将列表中的数据连接 就变成了 带空格的16进制数据
            # print(txDataHex)
            # self.plainTextEdit_Send.setPlainText(txDataHex)  # 显示

            txDataHex = binascii.hexlify(txData, " ").decode("utf-8")  # 转为16进制 字符串 并解码为 utf8 中间还插入 空格
            self.plainTextEdit_Send.setPlainText(txDataHex)  # 显示

        else:  # 最大支持到 7F 当前需要显示 utf8
            # 将发送框中的 16进制数据转为 utf8 显示
            print("16 to utf8")
            alist = []
            txData = self.plainTextEdit_Send.toPlainText()  # 获取到 utf8 数据
            print(txData)
            txData = txData.replace(" ", "")  # 将空格取消
            if len(txData) % 2 == 1:  # 去除独立数据
                txData = txData[0:len(txData) - 1]

            try:
                txDataHex = binascii.a2b_hex(txData).decode("utf-8")  # 转为 utf8字符串
            except:
                QMessageBox.critical(self, '严重错误', '该数据无法转换')
                self.checkBox_Send.stateChanged.disconnect(self.checkbox_send_cb)
                self.checkBox_Send.setCheckState(2)  # 0未选 1 半选 2选
                self.checkBox_Send.stateChanged.connect(self.checkbox_send_cb)

                return
                # for i in range(0, len(txData), 2):
                #     temp = txData[i:i+2]
                #     temp_hex = int(temp, 16)
                #     print(temp, type(temp))
                #     print(temp_hex, type(temp_hex))
                #     if temp_hex > 0x7F:
                #         alist.append("3F")
                #     else:
                #         alist.append(temp)
                #
                # txData = "".join(alist)
                # print(alist)
                # txDataHex = binascii.a2b_hex(txData).decode("utf-8")  # 转为 utf8字符串

            print(txDataHex)
            self.plainTextEdit_Send.setPlainText(txDataHex)  # 显示

    def checkbox_timer_cb(self):
        if self.checkBox_Send_Timer.isChecked():
            t = self.lineEdit_Send_Timer.text()

            if len(t) == 0:
                QMessageBox.critical(self, '严重错误', '请确认间隔')
                return
            t = int(t)
            self.timer_send.start(t)
        else:
            self.timer_send.stop()

    def pw_update(self):  # 数据更新时会触发也就是说 发送数据 和 接受数据都会触发的
        global pwData, pwData2, pwData3
        global pwDataarr, pwDataarr2, pwDataarr3
        global ptr1
        pwData2 = pwData
        pwData3 = pwData
        print("pwdata:", pwData)
        print("pwdata2:", pwData2)
        print("pwdata3:", pwData3)

        if len(pwData) > 0:  # 表示有数据 而不是空发
            # 处理 数据头 与 数据尾

            key = r"(?<={0})\d+(?=\D|\s*)".format(self.pwstart.text())
            print("key = ", key)
            ret = re.findall(key, pwData)  # 因为可能收到连续的 所以需要全部取出 使用findall
            if len(ret) > 0:
                if self.checkBox_pw.isChecked():  # 1111111111
                    for pwData in ret:  # 循环赋值
                        if len(pwDataarr) >= 6666:  # 最大数量
                            if pwData.isalnum():
                                pwDataarr.remove(pwDataarr[0])

                        if pwData.isalnum():  # 判断是否为全数字 可以减少错误警告
                            pwDataarr.append(int(pwData))

            key = r"(?<={0})\d+(?=\D|\s*)".format(self.pwstart_2.text())
            print("key = ", key)
            ret = re.findall(key, pwData2)
            if len(ret) > 0:
                if self.checkBox_pw_2.isChecked():  # 222222222
                    for pwData2 in ret:
                        if len(pwDataarr2) >= 6666:  # 最大数量
                            if pwData2.isalnum():
                                pwDataarr2.remove(pwDataarr2[0])

                        if pwData2.isalnum():  # 判断是否为全数字 可以减少错误警告
                            pwDataarr2.append(int(pwData2))

            key = r"(?<={0})\d+(?=\D|\s*)".format(self.pwstart_3.text())
            print("key = ", key)
            ret = re.findall(key, pwData3)
            if len(ret) > 0:
                if self.checkBox_pw_3.isChecked():  # 333333333
                    for pwData3 in ret:
                        if len(pwDataarr3) >= 6666:  # 最大数量
                            if pwData3.isalnum():
                                pwDataarr3.remove(pwDataarr3[0])

                        if pwData3.isalnum():  # 判断是否为全数字 可以减少错误警告
                            pwDataarr3.append(int(pwData3))

        pwData = ''

        self.pw1.clear()
        self.pw1.plot().setData(pwDataarr, pen='r')
        self.pw1.plot().setData(pwDataarr2, pen='g')
        self.pw1.plot().setData(pwDataarr3, pen='b')

        ptr1 += 1
        self.pw1.plot().setPos(ptr1, 0)

    def pw_cleandata(self):
        global pwData
        global pwDataarr
        pwData = ''
        pwDataarr.clear()

        self.pw1.clear()
        self.pw1.plot().setData(pwDataarr, pen='r')
        self.pw1.plot().setData(pwDataarr2, pen='g')
        self.pw1.plot().setData(pwDataarr3, pen='b')

    def pw_cleandata2(self):
        global pwData2
        global pwDataarr2

        pwData2 = ''
        pwDataarr2.clear()

        self.pw1.clear()
        self.pw1.plot().setData(pwDataarr, pen='r')
        self.pw1.plot().setData(pwDataarr2, pen='g')
        self.pw1.plot().setData(pwDataarr3, pen='b')

    def pw_cleandata3(self):
        global pwData3
        global pwDataarr3

        pwData3 = ''
        pwDataarr3.clear()

        self.pw1.clear()
        self.pw1.plot().setData(pwDataarr, pen='r')
        self.pw1.plot().setData(pwDataarr2, pen='g')
        self.pw1.plot().setData(pwDataarr3, pen='b')

    def mouseClicked(self, MouseClickEvent):
        vb1 = self.pw1.vb
        print([MouseClickEvent.scenePos().x(), MouseClickEvent.scenePos().y()])
        mousePoint = vb1.mapSceneToView(MouseClickEvent.scenePos())
        print(mousePoint.x(), mousePoint.y())
        x = float(mousePoint.x())
        y = float(mousePoint.y())
        self.pw1.setTitle("小灰灰^_^---时间  X=%0.2f  高度  Y=%0.2f" % (x, y))

        # # 显示双轴线  每次都会出现一条新的 不太方便
        # vLine1 = pg.InfiniteLine(angle=90, movable=False)
        # hLine1 = pg.InfiniteLine(angle=0, movable=False)
        # self.pw1.addItem(vLine1, ignoreBounds=True)
        # self.pw1.addItem(hLine1, ignoreBounds=True)
        #
        # vLine1.setPos(mousePoint.x())
        # hLine1.setPos(mousePoint.y())
