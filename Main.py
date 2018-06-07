"""
Iridium monitoring program for AirCore tracking and cutdown controls

Author: Ethan Fison, CS, MSGC
Purpose: Monitoring data from an Iridium modem used to track the location of an AirCore payload
Creation Date: June 2018
"""

# Imports
import sys
import datetime
import threading

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math
import MySQLdb

from trckGUI import Ui_Dialog


class MainWindow(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.closeBtn.clicked.connect(self.close)
        self.cutdownBtn.clicked.connect(self.cut)
        self.openBtn.clicked.connect(self.open)
        self.idleBtn.clicked.connect(self.idle)

    def close(self):
        print('Attempting to close valve')

    def cut(self):
        print("Attempting cutdown")

    def idle(self):
        print("Telling modem to idle")

    def open(self):
        print("Attempting to open valve")

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()

prog = MainWindow(dialog)

dialog.show()
sys.exit(app.exec_())
