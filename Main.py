"""
Iridium monitoring program for AirCore tracking and cutdown controls

Author: Ethan Fison, CS, MSGC
Based on the groundstation tracking software previously written by MSGC groups
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
from dataGrabber import GetData


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
    newCoords = pyqtSignal(GetData)

    no_iridium = pyqtSignal()

    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.cmdThread = EventThread()
        self.cmdThread.daemon = True
        self.iridium_thread = EventThread()
        self.iridium_thread.daemon = True
        self.iridium_thread.start()
        self.cmdThread.start()

        # Setup for the main window buttons
        self.closeBtn.clicked.connect(self.close_valve)
        self.cutdownBtn.clicked.connect(self.attempt_cutdown)
        self.openBtn.clicked.connect(self.open_valve)
        self.idleBtn.clicked.connect(self.send_idle)
        self.trckBtn.clicked.connect(self.start_tracking)

        self.db_host = 'eclipse.rci.montana.edu'
        self.db_user = 'antenna'
        self.db_pass = 'tracker'
        self.db_name = 'freemanproject'

        self.IMEI = ''
        self.email = ''
        self.passwd = ''
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setWindowTitle('ERROR - Missing Information')
        self.error_dialog.setModal(True)

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
        if self.IMEIBox.text() == '':
            # Ideally, there will be an error message that pops up here instead of just printing the error
            self.error_dialog.showMessage('Please enter an IMEI')
            print('No IMEI entered, please enter one before starting tracking')
        else:
            self.IMEI = str(self.IMEIBox.text())
            self.getData = GetData(self, self.db_host, self.db_user, self.db_pass, self.db_name, self.IMEI)
            self.getData.moveToThread(self.iridium_thread)
            self.GetData.set_interrupt.connect(self.getData.interrupt())
            self.getData.start.emit()
            print('Initializing tracking for modem with IMEI %s' % self.IMEI)

    def fetch_email(self):
        if self.gmail.text() == '' or self.gPass.text() == '':
            self.error_dialog.showMessage('Please check that both the email and password fields are not empty')
        else:
            self.email = self.gmail.text()
            self.passwd = self.gPass.text()
        # This line probably isn't secure, but I'm still pretty new to python, so what can you do?

    def update_position(self, new_data):
        if ((new_data.get_lat() == 0.0) or (new_data.get_lon == 0.0) or (new_data.get_alt() == 0.0)):
            return

        if new_data.get_seconds() < self.current.get_seconds():
            return


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()

prog = MainWindow(dialog)

dialog.show()
sys.exit(app.exec_())
