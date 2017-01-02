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

# 通过QToolBar创建工具栏


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口标题
        self.setWindowTitle("我的第一个窗口")
        # 新建一个标签
        label = QLabel("欢迎打开我的窗口")
        # 标签居中显示
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        # 定义一个工具栏
        tb = QToolBar('ToolBar')
        tb.setIconSize(QSize(16, 16))
        self.addToolBar(tb)

        button_action = QAction(QIcon('../icons/penguin.png'), 'Menu button', self)
        button_action.setStatusTip('This is menu button')
        button_action.triggered.connect(self.onButtonClick)
        button_action.setCheckable(True)
        tb.addAction(button_action)
        self.setStatusBar(QStatusBar(self))

    def onButtonClick(self, s):
        print(s)

# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
