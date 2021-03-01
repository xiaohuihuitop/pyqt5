from PyQt5.QtWidgets import QApplication
import serial
import graph


# import pyqtgraph.examples
# pyqtgraph.examples.run()

ui_app = QApplication([])
# main_win = serial.GetWin()
main_win = graph.GraphWin()
main_win.show()

ui_app.exec_()
