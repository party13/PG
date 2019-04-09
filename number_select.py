# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'number_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 298)
        self.number_submit = QtWidgets.QPushButton(Dialog)
        self.number_submit.setGeometry(QtCore.QRect(150, 160, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number_submit.setFont(font)
        self.number_submit.setObjectName("number_submit")
        self.number_input = QtWidgets.QLineEdit(Dialog)
        self.number_input.setGeometry(QtCore.QRect(110, 30, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.number_input.setFont(font)
        self.number_input.setObjectName("number_input")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.number_submit.setText(_translate("Dialog", "Далі"))

