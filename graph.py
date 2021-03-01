from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QCheckBox
from ui.graph_ui import Ui_Form

import pyqtgraph as pg
import pandas as pd
import numpy as np

class GraphWin(QMainWindow, Ui_Form):
    def __init__(self):
        super(GraphWin, self).__init__()
        self.setupUi(self)

        self.pw = pg.PlotWidget(self)  # 创建一个绘图控件
        # 要将pyqtgraph的图形添加到pyqt5的部件中，我们首先要做的就是将pyqtgraph的绘图方式由window改为widget。PlotWidget方法就是通过widget方法进行绘图的
        self.pw.resize(400, 200)
        self.pw.move(10, 10)
        data = np.random.random(size=50)
        self.pw.plot(data)  # 在绘图控件中绘制图形

