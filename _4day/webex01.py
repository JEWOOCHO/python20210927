# web 연습 01

# web1.py 
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#페이지 로딩
#연속적으로 메소드나 함수를 호출: 메서드 체인 
page = open("D:\\WORK\\python\\_4day\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체 생성: 정해진 문자열(html문서, xml은 주로 데이터 저장과 교환)
soup = BeautifulSoup(page, "html.parser")
#전체 페이지를 보기
#print( soup.prettify() )

#문서 내부에 <p> 모두 검색: List로 담아서 리턴 
#print( soup.find_all("p") ) 
#문서 내부에 <b>태그 몽땅
#print( soup.find_all("b") )
#첫번째 <p>를 가져오기 
#print( soup.find("p") )

#조건이 있는 경우: <p class="outer-text">
#파이썬의 키워드로 class가 제공되서 충돌을 피하기 위해 class_를 사용 
#print( soup.find_all("p", class_="outer-text") )

#태그 안쪽에 문자열을 검색: .text 속성을 사용 
#<p> 문자열 </p>
for tag in soup.find_all("p"):
    title = tag.text 
    title2 = title.replace("\n", "")
    title2 = title2.replace("\t", "")
    print( title2.strip() )
    #lst = title2.split()
    #print( lst )

