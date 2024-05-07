# ch 6.4.1 ctrl.py
## UI에서 입력되는 이벤트 처리, UI 동작 제어 관련 내용 포함
## 계산기의 덧셈 기능에 사용할 sum함수 구현


class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def calculate(self):  # 내용은 추후 작성
        pass

    def sum(self, a, b):  # 덧셈 함수 추가
        return a + b
