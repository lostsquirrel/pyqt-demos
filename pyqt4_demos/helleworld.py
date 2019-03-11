# encoding utf-8

import sys
from PyQt5.QtWidgets import QApplication, QLabel


def window():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec_()


if __name__ == '__main__':
    window()