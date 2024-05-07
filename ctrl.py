# ch 6.6.7 ctrl.py
## UI에서 입력되는 이벤트 처리, UI 동작 제어 관련 내용 포함
## calculate, connectSignals 함수 수정


class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(
        self,
    ):  # btn1을 클릭하면 calculate의 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def calculate(self):
        num1 = float(
            self.view.le1.text()
        )  # 첫 번째 라인 에디트에 입력된 숫자를 읽어 옴
        num2 = float(
            self.view.le2.text()
        )  # 두 번째 라인 에디트에 입력된 숫자를 읽어 옴
        operator = self.view.cb.currentText()  # 콤보 박스에 선택된 연산자 확인

        if operator == "+":
            return f"{num1} + {num2} = {self.sum(num1, num2)}"
        else:
            return "Calculation Error"

    def sum(self, a, b):  # 예외처리 제거 : 향후 calculate 함수에서 처리하도록 구현 예정
        return a + b
