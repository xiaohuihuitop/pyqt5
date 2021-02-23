from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit
from PyQt5.QtCore import QSettings, QIODevice  # 配置文件使用
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo  # 使用qt提供的串口工具 serial 这个模块是python的
from ui.win import Ui_MainWindow

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

        # 设置
        if self.baud is None:
            self.baud = 9600
            self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存

        # 赋值
        self.comboBox_baud.setCurrentText(self.baud)

        # 串口类
        self.com = QSerialPort()

        # 信号槽
        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.pushButton.clicked.connect(self.button_refresh_cb)   # 刷新端口
        self.pushButton_open.clicked.connect(self.button_open_cb)  # 打开端口
        self.pushButton_close.clicked.connect(self.button_close_cb)  # 关闭端口

        self.pushButton_send.clicked.connect(self.button_send_cb)  # 发送据数
        # self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 这里连接无效 需要在打开com口后再链接
        self.pushButton_clean.clicked.connect(self.button_clean_cb)  # 清除按钮

        # 自动滚屏
        self.plainTextEdit_Receive.textChanged.connect(self.text_scroll)

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()
        self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存

    def button_refresh_cb(self):
        com_list = QSerialPortInfo.availablePorts()  # 获取所有的端口信息
        for com in com_list:
            print(com.portName())  # 返回串口号，如COM1
            print(com.description())  # 返回设备硬件描述 如USB-SERIAL CH340
            print(com.productIdentifier())  # 返回设备编号 如29987
            print(com.standardBaudRates())  # 返回设备的支持波特率列表 如[110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200, 128000, 256000]
            if com.portName() is not None:  # 判断是否为空
                pass
                if self.comboBox_com.findText(com.portName()) < 0:  # 判断com口是否重复
                    print(self.comboBox_com.findText(com.portName()))  # 测试
                    self.comboBox_com.addItem(com.portName())  # 添加item


    def button_open_cb(self):
        print("open")
        port = self.comboBox_com.currentText()  # 获取 COM名字
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
            self.com.setDataBits(self.com.Data8)  # 8
            self.com.setParity(self.com.NoParity)  # n
            self.com.setStopBits(self.com.OneStop)  # 1
            self.com.setFlowControl(self.com.NoFlowControl)
            print("set over")
            print(self.com.baudRate())  # 验证波特率

            self.com.readyRead.connect(self.com_receive_cb)  # 接收数据 需要打开串口后再调用 此处有效
        pass

    def button_close_cb(self):
        print("close")
        port = self.comboBox_com.currentText()
        print(port)
        self.com = QSerialPort()
        self.com.setPortName(port)
        self.com.close()
        pass

    def button_send_cb(self):
        print("send")
        txData = self.plainTextEdit_Send.toPlainText()
        print(txData)
        print(txData.encode('UTF-8'))
        self.com.write(txData.encode('UTF-8'))

    def com_receive_cb(self):
        print("receive_cb")
        rxData = bytes(self.com.readAll())
        if len(rxData) > 0:
            try:
                # print(rxData.decode('ascii'))  ## 测试
                self.plainTextEdit_Receive.insertPlainText(rxData.decode('utf-8')) # ANSI UTF-8 GB2312  ISO-8859-1
            except:
                self.plainTextEdit_Receive.insertPlainText(rxData.decode('ISO-8859-1'))  # ANSI UTF-8 GB2312  ISO-8859-1


    def button_clean_cb(self):
        print("clean")
        self.plainTextEdit_Receive.clear()

    def text_scroll(self):
        self.plainTextEdit_Receive.verticalScrollBar().setValue(self.plainTextEdit_Receive.verticalScrollBar().maximum())


ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
