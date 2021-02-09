from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.win import Ui_MainWindow

num = 0


class GetWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GetWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Button_Call)
        self.tabWidget.currentChanged.connect(self.Tab_Call)

    def Lcd_Show(self):
        pass


    def Button_Call(self):
        global num
        if self.lineEdit.text().isdigit():  # 只有纯数字才获取
            num = int(self.lineEdit.text())
            num = num + 1
            self.lineEdit.setText(str(num))
            # self.lcdNumber.display(num)
            print("num={}".format(num))
        else:
            QMessageBox.information(self, "Hint", "非数字不能累加", QMessageBox.No | QMessageBox.Close)
            print("err")
            pass

    def Tab_Call(self):
        if self.tabWidget.currentIndex() == 0:
            print("0")
        elif self.tabWidget.currentIndex() == 1:
            print("1")
        else:
            pass



ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
