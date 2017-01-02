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
# Qt还支持自定义信号，可以通过创建pyqtSignal对象实例来定义信号对象


class MainWindow(QMainWindow):
    my_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口标题
        self.setWindowTitle("MainWindow")
        layout = QHBoxLayout()

        button = QPushButton("点我点我！！")
        button.pressed.connect(self._click_button)
        self.my_signal.connect(self._my_func)
        self.setCentralWidget(button)

    def _click_button(self):
        self.my_signal.emit('haha?')

    def _my_func(self, s):
        print(s)

# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
