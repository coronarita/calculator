# ch 5.2.1 ui.py

## main.py의 Calculator 클래스에서 화면정의, 초기화, 에디트 화면처리 분리

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
)

from PyQt5.QtGui import QIcon


class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton("Message", self)
        self.btn2 = QPushButton("Clear", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 공백
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()  # 수직 레이아웃
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)  # 빈 공간

        self.setLayout(vbox)  # 수직 배치 된 레이아웃 설정

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)
        self.show()

    def activeMessage(self):
        # QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button Clicked!")

    def clearMessage(self):
        self.te1.clear()
