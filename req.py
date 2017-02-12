# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebView

#import stuff_rc


url = "http://kuznech.com"
data = load(url)
print(data)