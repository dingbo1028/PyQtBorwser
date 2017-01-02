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

# Qt中每种组件都有所谓的信号槽（slot）机制。可用来将信号与相应地处理函数进行连接绑定
# 进一步说明信号槽，用按钮事件模拟


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口标题
        self.setWindowTitle("MainWindow")
        layout = QHBoxLayout()

        for i in range(5):
            button = QPushButton(str(i))
            # 按钮的按压信号关联
            button.pressed.connect(lambda x=i: self._my_func(x))
            layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _my_func(self, n):
        print('click button %s' % n)

# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
