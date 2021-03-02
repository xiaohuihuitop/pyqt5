from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPlainTextEdit, QCheckBox
from ui.graph_ui import Ui_Form

# import pyqtgraph as pg
# import pandas as pd
import numpy as np

class GraphWin(QMainWindow, Ui_Form):
    def __init__(self):
        super(GraphWin, self).__init__()
        self.setupUi(self)
        data = np.random.random(size=50)
        self.graphicsView.plot(data)

