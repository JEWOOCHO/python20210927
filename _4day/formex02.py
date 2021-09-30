

# form.py(로직 코딩) + form.ui(화면을 XML문서 저장)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩
#폼이 한개

form_class = uic.loadUiType("qt-window.ui")[0]
#윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 연습")
    def firstClick(self):
        self.label.setText("1 클릭")
    def secondClick(self):
        self.label.setText("2 클릭")
    def thirdClick(self):
        self.label.setText("3 클릭")



#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    d1 = DemoForm()
    d1.show()   
    app.exec_()
