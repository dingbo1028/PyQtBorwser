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


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 将QMainWindow的信号windowTitleChanged与_my_func槽参数相绑定
        # 当窗口标题被更改的信号发出的时候便会触发函数_my_func进行处理
        self.windowTitleChanged.connect(self._my_func)
        # 窗口标题
        self.setWindowTitle("我的第一个窗口")
        # 新建一个标签
        label = QLabel("欢迎打开我的第一个窗口")
        # 标签居中显示
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def _my_func(self, s='my_func', a=100):
        dic = {'s': s, 'a': a}
        print(dic)

# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
