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
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngine
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math
import MySQLdb

from trckGUI import Ui_Dialog


class EventThread(QThread):
    def run(self):
        self.exec_()


'''
class WebEngine(QtWebEngine):
    def console_message(self, line, msg, src):
        if src:
            print('Line(%s) Source(%s): %s' % (line, src, msg))
        else:
            print(msg)
'''


class MainWindow(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.cmdThread = EventThread()
        self.cmdThread.daemon = True
        # self.iridiumThread.start()
        self.cmdThread.start()

        self.closeBtn.clicked.connect(self.close_valve)
        self.cutdownBtn.clicked.connect(self.attempt_cutdown)
        self.openBtn.clicked.connect(self.open_valve)
        self.idleBtn.clicked.connect(self.send_idle)
        self.trckBtn.clicked.connect(self.start_tracking)

        self.IMEI = ''
        self.email = ''
        self.passwd = ''

    def close_valve(self):
        self.fetch_email()
        print('Attempting to close valve')

    def attempt_cutdown(self):
        self.fetch_email()
        print("Attempting cutdown")

    def send_idle(self):
        self.fetch_email()
        print("Telling modem to idle")

    def open_valve(self):
        self.fetch_email()
        print("Attempting to open valve")

    def start_tracking(self):
        self.IMEI = str(self.IMEIBox.text())
        print('Initializing tracking for modem with IMEI %s' % self.IMEI)

    def fetch_email(self):
        self.email = self.gmail.text()
        self.passwd = self.gPass.text()
        # This line probably isn't secure, but I'm still pretty new to python, so
        # what can you do?


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()

prog = MainWindow(dialog)

dialog.show()
sys.exit(app.exec_())
