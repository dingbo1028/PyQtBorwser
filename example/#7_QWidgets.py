#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: TingJoyshow 
@file: #1_start.py
@time: 2017-01-02 12:41
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# 小部件


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口标题
        self.setWindowTitle("QWidgets小部件演示")

        layout = QVBoxLayout()

        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]
        for item in widgets:
            layout.addWidget(item())
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
