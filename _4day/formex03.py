

# form.py(로직 코딩) + form.ui(화면을 XML문서 저장)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup


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
        function1()
        self.label.setText("1 작업완료")

    def secondClick(self):
        self.label.setText("2 클릭")
    def thirdClick(self):
        self.label.setText("3 클릭")


def function1():
    # 주석: ctrl + / 
    # <td class="title">
    # 	<a href="/webtoon/detail?titleId=2">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # </td>
    f = open("webtoon-ui.txt", "wt", encoding="utf-8")          
    for i in range(0,6):
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="+ str(i+1)
        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, "html.parser")                
        cartoons = soup.find_all("td", class_="title")

        #파일에 저장
        for item in cartoons:
            title = item.find("a").text
            link = item.find("a")["href"]
            text = "{0:40}{1:40}".format(title.strip() , link.strip())
            print(text)
            f.write(text+ "\n")

        f.write("\n")
    f.close()


#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    d1 = DemoForm()
    d1.show()   
    app.exec_()
