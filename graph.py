from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QCheckBox
from PyQt5 import QtCore
from ui.graph_ui import Ui_Form

import psutil
import traceback

import pyqtgraph as pg
import pandas as pd
import numpy as np

data1 = np.random.normal(size=50)
data1 = [0]
data2 = np.random.normal(size=2)
ptr1 = 0
class GraphWin(QMainWindow, Ui_Form):
    def __init__(self):
        super(GraphWin, self).__init__()

        # 这中间插入颜色设置  必须在 setupUi之前
        pg.setConfigOption('background', '#f0000f') # 背景颜色
        pg.setConfigOption('foreground', '#r') # 坐标轴颜色
        pg.setConfigOptions(antialias=True)
        #pg.setConfigOption('leftButtonPan', False)


        self.setupUi(self)

        self.pw.setTitle("Title", color='008080', size='12pt')
        self.pw.setLabel("left", "气温(摄氏度)")
        self.pw.setLabel("bottom", "时间")
        self.pw.setBackground('w') # 背景颜色

        self.pw.showGrid(x=True, y=True)  # 网格

        #self.pw.setXRange(max=100, min=0) # 设置范围
        #self.pw.setYRange(max=100, min=0) # 设置 范围

        self.pw.setClipToView(True)


        # data = np.random.random(size=50)
        # self.pw.plot(data, symbol='o', pen=pg.mkPen('g'))

        self.data_list = []

        self.timer = QtCore.QTimer(self) # 设置定时器
        self.timer.timeout.connect(self.update1) # 链接
        self.timer.start(50)  # 1秒钟一次

    def get_cpu_info(self):
        try:
            cpu = "%0.2f" % psutil.cpu_percent(interval=1)
            self.data_list.append(float(cpu))
            print(float(cpu))
            self.pw.plot().setData(self.data_list, pen='r')  # 显示
            #self.pw.plot(self.data_list, pen='g') # 显示 和上面那个效果一样的  所以会重叠
        except Exception as e:
            print(traceback.print_exc())
            
    def update1(self):
        global data1, ptr1, data2

        if len(data1) >= 20:
            data1.remove(data1[0])
        data1.append(np.random.normal())

        data2[1] = np.random.normal()

        #self.pw.clear()
        self.pw.plot().setData(data2, pen='r')

        ptr1 += 1
        self.pw.plot().setPos(ptr1, 0)

