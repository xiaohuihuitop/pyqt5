from PyQt5.QtWidgets import QApplication
import serial


ui_app = QApplication([])
main_win = serial.GetWin()
main_win.show()
ui_app.exec_()
