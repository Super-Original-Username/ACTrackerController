# This will eventually hold the code for retrieving tracking data from a database that will eventually be set up
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from dataUpdater import *
import MySQLdb

try:
    from urllib.request import urlopen
except ImportError:
    print("Library not found")


class GetData(QtCore.QObject):
    start = pyqtSignal()
    set_interrupt = pyqtSignal()

    def __init__(self, MainWindow, host, user, passwd, name, IMEI):
        super(GetData, self).__init__()
        self.mainWindow = MainWindow
        self.host = host
        self.user = user
        self.passwd = passwd
        self.name = name
        self.IMEI = IMEI
        self.inter = False

    def fetch_from_database(self):
        prev = ''
        connected = False
        attempts = 0
        while not connected and not self.inter:
            QtGui.QGuiApplication.processEvents()
            if attempts < 20:
                try:
                    database = MySQLdb.connect(host="eclipse.rci.montana.edu", user="antenna", passwd="tracker",
                                               db="freemanproject")
                    cmd = 'select gps_lat, gps_long, gps_alt, gps_time from gps where gps_IMEI = %s order by pri_key DESC LIMIT 1' % self.IMEI
                    database.query(cmd)
                    connected = True

                    if self.inter:
                        database.close()
                        connected = True
                except:
                    print('Failed to connect, reattempting in 1 second')
                    attempts += 1
            else:
                print('Too many attempts, quitting')
                self.interrupt()
                self.mainWindow.no_iridium.emit()
            if connected:
                try:
                    r = database.store_result()
                    results = r.fetch_row()
                    if results != prev:
                        prev = results
                        print(results)
                        time = results[0][3].split(':')
                        hours = int(time[0])
                        minutes = int(time[1])
                        seconds = int(time[2])
                        seconds = seconds + (60 * minutes) + (3600 * hours)
                        lat = float(results[0][0])
                        lon = float(results[0][1])
                        alt = float(results[0][2])

                        try:
                            new_loc = Updater(time, lat, lon, alt, seconds)
                        except:
                            print('Error updating from data')

                        try:
                            return new_loc
                        except Exception as e:
                            print(str(e))

                except:
                    print('ERROR: Could not find any data. Please check the IMEI for your modem')

        try:
            database.close()
        except:
            print('Could not close database')

    def interrupt(self):
        self.inter = True
