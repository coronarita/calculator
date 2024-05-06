# ch 5.4.1 ui.py

## main.py의 Calculator 클래스에서 화면정의, 초기화, 에디트 화면처리 분리
## 오늘 날짜 출력되도록 구현

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
    QLabel,
)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt  # 날짜와 주요 속성값 사용을 위해 추가


class View(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()  # 현재 날짜를 저장하기 위해 추가
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)
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
        vbox.addWidget(self.lbl1)
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
