from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QSettings
from ui.win import Ui_MainWindow

num = 0
path = None


class GetWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GetWin, self).__init__()
        self.setupUi(self)

        self.settings = QSettings("config.ini", QSettings.IniFormat)

        # 获取
        self.com = self.settings.value("SETUP/COM_VALUE")
        self.baud = self.settings.value("SETUP/BAUD_VALUE")

        # 设置
        if self.baud is None:
            self.baud = 9600
            self.settings.setValue("SETUP/BAUD_VALUE", self.baud) # 保存

        # 赋值
        self.comboBox_baud.setCurrentText(self.baud)

        # 信号槽
        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()
        self.settings.setValue("SETUP/BAUD_VALUE", self.baud)  # 保存


ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
