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
