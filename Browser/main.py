#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: TingJoyshow 
@file: main.py
@time: 2017-01-02 14:51
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("BoBrowser")
        self.setWindowIcon(QIcon('../icons/penguin.png'))
        self.show()

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tabs_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # 允许关闭标签
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.add_new_tab(QUrl('http://www.hao123.com'), "HomePage")
        self.setCentralWidget(self.tabs)

        # self.browser = QWebView()
        # url = "http://www.baidu.com"
        # self.browser.setUrl(QUrl(url))
        # self.setCentralWidget(self.browser)

        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon('../icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('../icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('../icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('../icons/renew.png'), 'Reload', self)

        back_button.triggered.connect(self.tabs.currentWidget().back)
        next_button.triggered.connect(self.tabs.currentWidget().forward)
        stop_button.triggered.connect(self.tabs.currentWidget().stop)
        reload_button.triggered.connect(self.tabs.currentWidget().reload)

        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        # 添加地址栏
        self.urlbar = QLineEdit()
        # 响应回车
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.tabs.currentWidget().setUrl(q)

    def renew_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def add_new_tab(self, qurl=QUrl(''), label='Blank'):
        browser = QWebView()
        browser.setUrl(qurl)
        # 添加索引
        i = self.tabs.addTab(browser, label)
        # self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.renew_urlbar(qurl, browser))

        # 加载完成之后添加标题
        browser.loadFinished.connect(lambda _, i=i, browswe=browser:
                                     self.tabs.setTabText(i, browser.page().mainFrame().title()))

    def close_current_tab(self, i):
        if self.tabs.count() <2:
            return
        self.tabs.removeTab(i)

    def tabs_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.renew_urlbar(qurl, self.tabs.currentWidget())

app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec_()
