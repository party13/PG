# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaymentComplete(object):
    def setupUi(self, PaymentComplete):
        PaymentComplete.setObjectName("PaymentComplete")
        PaymentComplete.resize(500, 500)
        self.print_check = QtWidgets.QPushButton(PaymentComplete)
        self.print_check.setGeometry(QtCore.QRect(10, 380, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.print_check.setFont(font)
        self.print_check.setObjectName("print_check")
        self.cancel = QtWidgets.QPushButton(PaymentComplete)
        self.cancel.setGeometry(QtCore.QRect(220, 360, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.label_10 = QtWidgets.QLabel(PaymentComplete)
        self.label_10.setGeometry(QtCore.QRect(80, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.duration_label = QtWidgets.QLabel(PaymentComplete)
        self.duration_label.setGeometry(QtCore.QRect(240, 90, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.duration_label.setFont(font)
        self.duration_label.setObjectName("duration_label")
        self.time_start_label = QtWidgets.QLabel(PaymentComplete)
        self.time_start_label.setGeometry(QtCore.QRect(240, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_start_label.setFont(font)
        self.time_start_label.setObjectName("time_start_label")
        self.label_11 = QtWidgets.QLabel(PaymentComplete)
        self.label_11.setGeometry(QtCore.QRect(176, 140, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(PaymentComplete)
        self.label_14.setGeometry(QtCore.QRect(180, 190, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.time_limit_label = QtWidgets.QLabel(PaymentComplete)
        self.time_limit_label.setGeometry(QtCore.QRect(240, 190, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_limit_label.setFont(font)
        self.time_limit_label.setObjectName("time_limit_label")
        self.auto_number_label = QtWidgets.QLabel(PaymentComplete)
        self.auto_number_label.setGeometry(QtCore.QRect(240, 250, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.auto_number_label.setFont(font)
        self.auto_number_label.setObjectName("auto_number_label")
        self.label_17 = QtWidgets.QLabel(PaymentComplete)
        self.label_17.setGeometry(QtCore.QRect(95, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(PaymentComplete)
        self.label_18.setGeometry(QtCore.QRect(110, 306, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.money_label = QtWidgets.QLabel(PaymentComplete)
        self.money_label.setGeometry(QtCore.QRect(240, 300, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.money_label.setFont(font)
        self.money_label.setObjectName("money_label")
        self.label_12 = QtWidgets.QLabel(PaymentComplete)
        self.label_12.setGeometry(QtCore.QRect(80, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(PaymentComplete)
        self.label_13.setGeometry(QtCore.QRect(90, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(PaymentComplete)
        QtCore.QMetaObject.connectSlotsByName(PaymentComplete)

    def retranslateUi(self, PaymentComplete):
        _translate = QtCore.QCoreApplication.translate
        PaymentComplete.setWindowTitle(_translate("PaymentComplete", "Dialog"))
        self.print_check.setText(_translate("PaymentComplete", "Надрукувати чек"))
        self.cancel.setText(_translate("PaymentComplete", "ЗБЕРЕЖІТЬ ДОВКІЛЛЯ"))
        self.label_10.setText(_translate("PaymentComplete", "ТРИВАЛІСТЬ"))
        self.duration_label.setText(_translate("PaymentComplete", "_"))
        self.time_start_label.setText(_translate("PaymentComplete", "_"))
        self.label_11.setText(_translate("PaymentComplete", "Від:"))
        self.label_14.setText(_translate("PaymentComplete", "До:"))
        self.time_limit_label.setText(_translate("PaymentComplete", "_"))
        self.auto_number_label.setText(_translate("PaymentComplete", "_"))
        self.label_17.setText(_translate("PaymentComplete", "Номер авто:"))
        self.label_18.setText(_translate("PaymentComplete", "Сплачено:"))
        self.money_label.setText(_translate("PaymentComplete", "_"))
        self.label_12.setText(_translate("PaymentComplete", "ПАРКУВАННЯ:"))
        self.label_13.setText(_translate("PaymentComplete", "ОПЛАТА УСПІШНА"))
