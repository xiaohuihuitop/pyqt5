from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
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
        self.com = self.settings.value("SETUP/COM_VALUE")
        self.baud = self.settings.value("SETUP/BAUD_VALUE")

        # 设置
        if self.baud is None:
            self.baud = 9600
            self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存

        # 赋值
        self.comboBox_baud.setCurrentText(self.baud)

        # 信号槽
        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.pushButton.clicked.connect(self.button_refresh_cb)
        self.pushButton_open.clicked.connect(self.button_open_cb)
        self.pushButton_close.clicked.connect(self.button_close_cb)

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()
        self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存

    def button_refresh_cb(self):
        com_list = QSerialPortInfo.availablePorts()
        for com in com_list:
            print(com.portName())  # 返回串口号，如COM1
            print(com.description())  # 返回设备硬件描述 如USB-SERIAL CH340
            print(com.productIdentifier())  # 返回设备编号 如29987
            print(com.standardBaudRates())  # 返回设备的支持波特率列表 如[110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200, 128000, 256000]
            if com.portName() is not None:
                pass
                if self.comboBox_com.findText(com.portName()) != 1:
                    self.comboBox_com.addItem(com.portName())


    def button_open_cb(self):
        print("open")
        port = self.comboBox_com.currentText()
        print(port)
        com = QSerialPort()
        com.setPortName(port)
        if com.open(QSerialPort.ReadWrite) == False: # QSerialPort  QIODevice
            print("open err")
        pass

    def button_close_cb(self):
        print("close")
        port = self.comboBox_com.currentText()
        print(port)
        com = QSerialPort()
        com.setPortName(port)
        com.close()
        pass

ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
