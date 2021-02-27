from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QCheckBox
from PyQt5.QtCore import QSettings, QIODevice, QTimer  # 配置文件使用
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo  # 使用qt提供的串口工具 serial 这个模块是python的
from PyQt5.QtGui import QIntValidator
from ui.win import Ui_MainWindow
import datetime
import binascii
num = 0
path = None


class GetWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GetWin, self).__init__()
        self.setupUi(self)

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

        self.pushButton.clicked.connect(self.button_refresh_cb)   # 刷新端口
        self.pushButton_open.clicked.connect(self.button_open_cb)  # 打开端口
        self.pushButton_close.clicked.connect(self.button_close_cb)  # 关闭端口

        self.pushButton_send.clicked.connect(self.button_send_cb)  # 发送据数
        # self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 这里连接无效 需要在打开com口后再链接
        self.pushButton_clean.clicked.connect(self.button_clean_cb)  # 清除按钮

        # 自动滚屏
        self.plainTextEdit_Receive.textChanged.connect(self.text_scroll)

        # 初始操作
        self.button_refresh_cb()
        self.pushButton_close.setDisabled(True)
        self.lineEdit_Send_Timer.setValidator(QIntValidator(0, 99999))

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
            print(com.standardBaudRates())  # 返回设备的支持波特率列表 如[110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200, 128000, 256000]
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

            #self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 需要打开串口后再调用 此处有效
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
        print("send")
        time_stamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
        print(time_stamp)

        if self.checkBox_Send.isChecked():
            txDataHex = self.plainTextEdit_Send.toPlainText()
            print(txDataHex)
            txData = txDataHex.replace(" ", "")  # 取消空格 准备转16进制
            txData = binascii.a2b_hex(txData).decode("utf-8")  # 转为 utf8字符串
            print(txData)
            self.com.write(txData.encode('UTF-8'))  # 编码为bytes再发送

            # 处理显示部分
            txDataHex = txDataHex.replace(" ", "")  # 取消空格
            print(txDataHex)

            alist = []
            #  将字符串 分割 加入列表
            for i in range(0, len(txDataHex), 2):
                alist.append(txDataHex[i:i+2])

            txDataHex = " ".join(alist)  # 使用 ” “ 空格 将列表中的数据连接 就变成了 带空格的16进制数据
            print(txDataHex)

            self.plainTextEdit_Receive.insertPlainText(time_stamp + "发->" + txDataHex + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
        else:
            txData = self.plainTextEdit_Send.toPlainText()
            print(txData)
            print(txData.encode('UTF-8'))
            self.com.write(txData.encode('UTF-8'))
            self.plainTextEdit_Receive.insertPlainText(time_stamp + "发->" + txData + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1



    def com_receive_cb(self):
        print("receive_cb")
        rxData = bytes(self.com.readAll())
        if len(rxData) > 0:
            time_stamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
            if not self.checkBox_Receive.isChecked():
                try:
                    # print(rxData.decode('ascii'))  ## 测试
                    self.plainTextEdit_Receive.insertPlainText(time_stamp + "收->")
                    self.plainTextEdit_Receive.insertPlainText(rxData.decode('utf-8') + "\n") # ANSI UTF-8 GB2312  ISO-8859-1
                except:
                    self.plainTextEdit_Receive.insertPlainText(rxData.decode('ISO-8859-1') + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
            else:
                try:
                    self.plainTextEdit_Receive.insertPlainText(time_stamp + "收->")
                    rxDataHex = binascii.hexlify(rxData, " ").decode("utf-8")  # 转为 utf8字符串
                    self.plainTextEdit_Receive.insertPlainText(rxDataHex + "\n") # ANSI UTF-8 GB2312  ISO-8859-1
                except:
                    rxDataHex = binascii.hexlify(rxData, " ").decode("ISO-8859-1")  # 转为 utf8字符串
                    self.plainTextEdit_Receive.insertPlainText(rxDataHex + "\n")  # ANSI UTF-8 GB2312  ISO-8859-1
                pass

    def button_clean_cb(self):
        print("clean")
        self.plainTextEdit_Receive.clear()

    def text_scroll(self):
        self.plainTextEdit_Receive.verticalScrollBar().setValue(self.plainTextEdit_Receive.verticalScrollBar().maximum())

    def checkbox_send_cb(self):
        if self.checkBox_Send.isChecked():  # 当前需要显示hex
            #  将 发送框中的数据转为 16进制
            print("utf8 to 16")
            alist = []
            txData = self.plainTextEdit_Send.toPlainText().encode('UTF-8') # 获取到数据 并转为 bytes
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
            self.plainTextEdit_Send.setPlainText(txDataHex) # 显示

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
                self.checkBox_Send.setCheckState(2) # 0未选 1 半选 2选
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
        t = self.lineEdit_Send_Timer.text()
        t = int(t)
        if self.checkBox_Send_Timer.isChecked():
            self.timer_send.start(t)
        else:
            self.timer_send.stop()


ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
