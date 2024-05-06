# ch 4.2.3 main.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

from PyQt5.QtGui import QIcon


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton("Message", self)
        self.btn1.clicked.connect(self.activeMessage)

        vbox = QVBoxLayout()  # 수직 레이아웃
        vbox.addStretch(1)  # 빈 공간
        vbox.addWidget(self.btn1)  # 버튼 위치
        vbox.addStretch(1)  # 빈 공간

        self.setLayout(vbox)  # 수직 배치 된 레이아웃 설정

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)
        self.show()

    def activeMessage(self):
        QMessageBox.information(self, "information", "Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
