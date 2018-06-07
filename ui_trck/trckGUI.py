# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\trckGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1298, 1027)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(890, 950, 371, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.historicCoords = QtWidgets.QTableWidget(Dialog)
        self.historicCoords.setGeometry(QtCore.QRect(10, 70, 891, 741))
        self.historicCoords.setObjectName("historicCoords")
        self.historicCoords.setColumnCount(0)
        self.historicCoords.setRowCount(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 201, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 830, 191, 25))
        self.label_2.setObjectName("label_2")
        self.currentCoords = QtWidgets.QTableWidget(Dialog)
        self.currentCoords.setGeometry(QtCore.QRect(10, 870, 891, 61))
        self.currentCoords.setObjectName("currentCoords")
        self.currentCoords.setColumnCount(0)
        self.currentCoords.setRowCount(0)
        self.cutdownBtn = QtWidgets.QPushButton(Dialog)
        self.cutdownBtn.setGeometry(QtCore.QRect(940, 70, 311, 46))
        self.cutdownBtn.setObjectName("cutdownBtn")
        self.idleBtn = QtWidgets.QPushButton(Dialog)
        self.idleBtn.setGeometry(QtCore.QRect(940, 160, 311, 46))
        self.idleBtn.setObjectName("idleBtn")
        self.openBtn = QtWidgets.QPushButton(Dialog)
        self.openBtn.setGeometry(QtCore.QRect(940, 260, 311, 46))
        self.openBtn.setObjectName("openBtn")
        self.closeBtn = QtWidgets.QPushButton(Dialog)
        self.closeBtn.setGeometry(QtCore.QRect(939, 340, 311, 46))
        self.closeBtn.setObjectName("closeBtn")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Historic Coordinates"))
        self.label_2.setText(_translate("Dialog", "Current Coordinates"))
        self.cutdownBtn.setText(_translate("Dialog", "Send Cutdown Command"))
        self.idleBtn.setText(_translate("Dialog", "Send Idle Command"))
        self.openBtn.setText(_translate("Dialog", "Open AirCore Valve"))
        self.closeBtn.setText(_translate("Dialog", "Close AirCore Valve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

