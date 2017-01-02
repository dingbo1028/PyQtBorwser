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

import sys

# Qt的执行机制：通过创建QApplication类实例来调用app.exec_方法进入事件循环
# 此时程序一直监听各种事件并把他们放到消息队列，在适当的时候取出队列进行处理


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口标题
        self.setWindowTitle("我的第一个窗口")
        # 新建一个标签
        label = QLabel("欢迎打开我的第一个窗口")
        # 标签居中显示
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
