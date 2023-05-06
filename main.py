import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QThread, QTimer, QSize
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSplashScreen, QDialog
import api


class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.enter_button.clicked.connect(self.enter)
        self.reg_button.clicked.connect(self.create_account)
        self.password_enter.textChanged.connect(self.hide_password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
