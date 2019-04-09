import sys
from PyQt5 import QtWidgets

import main_window
import number_select
import final
import utils, settings
from datetime import datetime, timedelta
from math import ceil

class SelectNumber(QtWidgets.QDialog, number_select.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.number = ''
        self.number_submit.clicked.connect(self.submitting)
        self.number_input.textChanged.connect(self.number_to_upper)

    def number_to_upper(self):
        text = self.number_input.text()
        self.number_input.setText(text.upper())

    def submitting(self):
        self.number = self.number_input.text()
        if self.number_check(self.number):
            self.hide()
        else:
            print('incorrect number')

    def number_check(self, number):
        if len(number) in range(3,9):
            return True

    def get_number(self):
        return self.number


class PaymentWindow(QtWidgets.QMainWindow, main_window.Ui_PaymentWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_time.setText(datetime.strftime(datetime.now(), "%H:%M:%S"))

        self.hours = 1
        self.minutes = 0    # possible values 0,1,2,3 which corresponds 00,15,30 and 45 minutes
        self.money = 0      # how much money have been verified by validator
        self.price = 15     # how much money the parking cost

        self.timelimit = datetime.now() + timedelta(hours=self.hours, minutes=15 * self.minutes)
        self.time_limit_label.setText(datetime.strftime(self.timelimit, "%H:%M:%S"))
        self.duration = 60

        self.BUY_button.clicked.connect(self.buy)
        self.plus_hours.clicked.connect(self.hours_up)
        self.minus_hours.clicked.connect(self.hours_down)
        self.plus_minutes.clicked.connect(self.minutes_up)
        self.minus_minutes.clicked.connect(self.minutes_down)

        self.moneySlider.setMinimum(0)
        self.moneySlider.setMaximum(300)
        self.moneySlider.valueChanged.connect(self.money_change)

        self.EnterNumberDialog()

    def EnterNumberDialog(self):
        window = SelectNumber()
        window.exec_()
        self.number = window.get_number()
        self.auto_number_label.setText(self.number)

    def money_change(self, value):
        self.money_received.setText(str(value))
        self.money = value
        self.check_price()

    def check_price(self):
        if self.money >= self.price:
            self.BUY_button.setEnabled(True)
        else:
            self.BUY_button.setEnabled(False)

    def hours_up(self):
        self.hours += 1
        self.hours_label.setText(str(self.hours))
        self.minus_hours.enabled = True

        self.count_price()

    def hours_down(self):
        if self.hours > 1:
            self.hours -= 1
            self.hours_label.setText(str(self.hours))
        self.count_price()

    def minutes_up(self):
        self.minutes += 1
        if self.minutes > 3:
            self.minutes = 0
            self.hours_up()
        self.minutes_label.setText(str(self.minutes * 15))
        self.count_price()

    def minutes_down(self):
        self.minutes -= 1
        if self.minutes < 0:
            if self.hours > 1:
                self.minutes = 3
                self.hours_down()
            else:
                self.minutes = 0

        self.minutes_label.setText(str(self.minutes * 15))
        self.count_price()

    def count_price(self):
        tariff = 1
        self.duration = self.hours * 60 + self.minutes * 15
        self.price = tariff * 15 * ceil(self.duration / 60)
        self.timelimit = datetime.now() + timedelta(hours=self.hours, minutes=15 * self.minutes)

        self.time_limit_label.setText(datetime.strftime(self.timelimit, "%H:%M:%S"))
        self.current_time.setText(datetime.strftime(datetime.now(), "%H:%M:%S"))

        self.BUY_button.setText(str(self.price))
        self.check_price()

    def buy(self):
        # number = 'АЕ1234АН'
        # price = '15.00'
        # tariff = '01'
        utils.send_packet(self.number, self.price, self.duration)

        self.hide()
        self.showFinalDialog()
        self.close()
        utils.send_packet(self.number, self.price, self.duration)
        print('send')

    def showFinalDialog(self):
        window = Final_window(self.number, self.duration, self.timelimit, self.price)
        window.exec_()


class Final_window(QtWidgets.QDialog, final.Ui_PaymentComplete):
    def __init__(self, number, duration, timelimit, price):
        super().__init__()
        self.setupUi(self)

        self.number = number
        self.duration = duration
        self.timelimit = timelimit
        self.price = price
        self.starttime = timelimit - timedelta(minutes=duration)

        self.auto_number_label.setText(str(number) )
        self.duration_label.setText(str(duration) + ' хвилин')
        self.time_limit_label.setText(datetime.strftime(self.timelimit, "%H:%M:%S"))
        self.money_label.setText(str(price) + ' грн')

        self.time_start_label.setText(datetime.strftime(self.starttime, "%H:%M:%S"))

        self.print_check.clicked.connect(self.printing)
        self.cancel.clicked.connect(self.eco)

    def printing(self):
        print('Паркомат : {}'.format(settings.DEVICE_NUMBER))
        print('Час: {}\n'
              'Сплачено {} хвилин.\n'
              'Від: {}\n'
              'До: {}\n'
              '------\n'
              'Номер Авто: {}\n'
              'Сума: {} грн'.format(datetime.strftime(datetime.now(), "%H:%M:%S"),
                                    self.duration,
                                    datetime.strftime(self.starttime, "%H:%M:%S"),
                                    datetime.strftime(self.timelimit, "%H:%M:%S"),
                                    self.number,
                                    self.price))
        self.close()

    def eco(self):
        print('Дякуємо за збереження довкілля!')
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()