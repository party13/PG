# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaymentWindow(object):
    def setupUi(self, PaymentWindow):
        PaymentWindow.setObjectName("PaymentWindow")
        PaymentWindow.setEnabled(True)
        PaymentWindow.resize(500, 501)
        PaymentWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(PaymentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.minus_hours = QtWidgets.QPushButton(self.centralwidget)
        self.minus_hours.setGeometry(QtCore.QRect(34, 104, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.minus_hours.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus_hours.setFont(font)
        self.minus_hours.setObjectName("minus_hours")
        self.plus_hours = QtWidgets.QPushButton(self.centralwidget)
        self.plus_hours.setGeometry(QtCore.QRect(134, 104, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.plus_hours.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus_hours.setFont(font)
        self.plus_hours.setObjectName("plus_hours")
        self.hours_label = QtWidgets.QLabel(self.centralwidget)
        self.hours_label.setGeometry(QtCore.QRect(94, 104, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.hours_label.setFont(font)
        self.hours_label.setObjectName("hours_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(234, 104, 16, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.minutes_label = QtWidgets.QLabel(self.centralwidget)
        self.minutes_label.setGeometry(QtCore.QRect(354, 104, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minutes_label.setFont(font)
        self.minutes_label.setObjectName("minutes_label")
        self.plus_minutes = QtWidgets.QPushButton(self.centralwidget)
        self.plus_minutes.setGeometry(QtCore.QRect(404, 104, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.plus_minutes.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus_minutes.setFont(font)
        self.plus_minutes.setObjectName("plus_minutes")
        self.minus_minutes = QtWidgets.QPushButton(self.centralwidget)
        self.minus_minutes.setGeometry(QtCore.QRect(294, 104, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.minus_minutes.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus_minutes.setFont(font)
        self.minus_minutes.setObjectName("minus_minutes")
        self.BUY_button = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_button.setEnabled(False)
        self.BUY_button.setGeometry(QtCore.QRect(80, 240, 341, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.BUY_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(58)
        self.BUY_button.setFont(font)
        self.BUY_button.setObjectName("BUY_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(34, 154, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 150, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 250, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.moneySlider = QtWidgets.QSlider(self.centralwidget)
        self.moneySlider.setGeometry(QtCore.QRect(130, 430, 160, 19))
        self.moneySlider.setOrientation(QtCore.Qt.Horizontal)
        self.moneySlider.setObjectName("moneySlider")
        self.money_received = QtWidgets.QLabel(self.centralwidget)
        self.money_received.setGeometry(QtCore.QRect(400, 422, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.money_received.setFont(font)
        self.money_received.setObjectName("money_received")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 410, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 360, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.time_limit_label = QtWidgets.QLabel(self.centralwidget)
        self.time_limit_label.setGeometry(QtCore.QRect(290, 356, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.time_limit_label.setFont(font)
        self.time_limit_label.setObjectName("time_limit_label")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.current_time = QtWidgets.QLabel(self.centralwidget)
        self.current_time.setGeometry(QtCore.QRect(280, 0, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.current_time.setFont(font)
        self.current_time.setObjectName("current_time")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 47, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 320, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.auto_number_label = QtWidgets.QLabel(self.centralwidget)
        self.auto_number_label.setGeometry(QtCore.QRect(240, 312, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.auto_number_label.setFont(font)
        self.auto_number_label.setObjectName("auto_number_label")
        PaymentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PaymentWindow)
        self.statusbar.setObjectName("statusbar")
        PaymentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PaymentWindow)
        QtCore.QMetaObject.connectSlotsByName(PaymentWindow)
        PaymentWindow.setTabOrder(self.minus_hours, self.plus_hours)
        PaymentWindow.setTabOrder(self.plus_hours, self.minus_minutes)
        PaymentWindow.setTabOrder(self.minus_minutes, self.plus_minutes)
        PaymentWindow.setTabOrder(self.plus_minutes, self.BUY_button)

    def retranslateUi(self, PaymentWindow):
        _translate = QtCore.QCoreApplication.translate
        PaymentWindow.setWindowTitle(_translate("PaymentWindow", "MainWindow"))
        self.minus_hours.setText(_translate("PaymentWindow", "-"))
        self.plus_hours.setText(_translate("PaymentWindow", "+"))
        self.hours_label.setText(_translate("PaymentWindow", "01"))
        self.label_2.setText(_translate("PaymentWindow", ":"))
        self.minutes_label.setText(_translate("PaymentWindow", "00"))
        self.plus_minutes.setText(_translate("PaymentWindow", "+"))
        self.minus_minutes.setText(_translate("PaymentWindow", "-"))
        self.BUY_button.setText(_translate("PaymentWindow", "15"))
        self.label_4.setText(_translate("PaymentWindow", "ДО СПЛАТИ"))
        self.label_5.setText(_translate("PaymentWindow", "мінімум : 1 година"))
        self.label_6.setText(_translate("PaymentWindow", "крок : 15 хвилин"))
        self.label_7.setText(_translate("PaymentWindow", "$"))
        self.money_received.setText(_translate("PaymentWindow", "0"))
        self.label_8.setText(_translate("PaymentWindow", "Внесено:"))
        self.label_9.setText(_translate("PaymentWindow", "Буде сплачено до:"))
        self.time_limit_label.setText(_translate("PaymentWindow", "_"))
        self.label_11.setText(_translate("PaymentWindow", "Зараз:"))
        self.current_time.setText(_translate("PaymentWindow", "_"))
        self.label_10.setText(_translate("PaymentWindow", "ТРИВАЛІСТЬ ПАРКУВАННЯ"))
        self.label_12.setText(_translate("PaymentWindow", "Номер машини:"))
        self.auto_number_label.setText(_translate("PaymentWindow", "_"))
