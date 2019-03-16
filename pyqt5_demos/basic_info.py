# encoding utf-8

import sys
from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QGridLayout)

start_time = datetime.now()


def change_label(lb, content):
    lb.setText(content)


class UptimeLable(QLabel):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.update_content()

    def update_content(self):
        # print('update')
        delta = (datetime.now() - start_time)
        seconds = delta.seconds
        hour = seconds // 3600
        seconds -= (hour * 3600)
        min = seconds // 60
        seconds -= min * 60
        self.setText("%d 天 %d 时 %d 分 %d 秒" % (delta.days, hour, min, seconds))


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('OPC 采集状态')
        self.uptime_timer = QtCore.QTimer()
        self.init_ui()

        # timer.startTimer()
        # print(timer)

    def init_ui(self):

        uptime_key = QLabel('运行时间：')
        uptime = UptimeLable()

        self.uptime_timer.timeout.connect(uptime.update_content)
        self.uptime_timer.setSingleShot(False)
        self.uptime_timer.setInterval(1000)
        self.uptime_timer.start(1000)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(uptime_key)
        grid.addWidget(uptime)
        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())
