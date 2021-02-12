from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui.win import Ui_MainWindow

num = 0
path = None


class GetWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GetWin, self).__init__()
        self.setupUi(self)

        # 链接槽
        self.actionopen.triggered.connect(self.open_file)
        self.actionsave.triggered.connect(self.save_file)
        self.actionsave_as.triggered.connect(self.save_file_as)




    def open_file(self):
        global path
        print("open")
        path = QFileDialog.getOpenFileName(self, "请选择文件")[0]  # 返回的是一个元组数据，第一个成员是文件名
        print(path)
        if path is not None:
            # QMessageBox.information(self, "提示", path)
            # self.textEdit.setText(open(path,mode='rb+').read().decode("utf-8"))
            with open(path, mode='rb+') as f:
                self.textEdit.setText(f.read().decode("utf-8"))
        else:
            # QMessageBox.information(self, "提示", "未正确选择文件")
            pass

    def save_file(self):
        global path
        if path is not None:
            with open(path, mode='wb') as f:
                f.write(self.textEdit.toPlainText().encode("utf-8"))
            self.textEdit.document().setModified(False)  # 文件修改标志清除


    def save_file_as(self):
        global path
        file = QFileDialog.getSaveFileName(self, "另存为", path)[0]
        if file is not None:
            path = file
            self.save_file()



ui_app = QApplication([])
main_win = GetWin()
main_win.show()
ui_app.exec_()
