# ch 6.2.2 ctrl.py
## UI에서 입력되는 이벤트 처리, UI 동작 제어 관련 내용 포함
## btn1 클릭 시 계산하도록 구현


class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def calculate(self):  # 내용은 추후 작성
        pass
