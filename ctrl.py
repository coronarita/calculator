# ch 5.2.1 ctrl.py
## UI에서 입력되는 이벤트 처리, UI 동작 제어 관련 내용 포함


class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activeMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)
