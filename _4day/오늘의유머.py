# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#우리 사이트는 웹봇을 금지 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("D:\WORK\python\_4day\\오늘의유머.txt", "wt", encoding="utf-8")
for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우에는 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <td class="subject">
        #     <a href="/board/view.php">넷플릭스가 한국 컨텐츠에 얼마나 진심인지를 알아보자</a>

        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.find("a").text.strip()  
                        title = title.replace("\t", "")
                        #print( title )
                        #정규표현식을 사용해서 검색
                        if (re.search("이재명", title)):
                                print( title )
                                f.write( title + "\n")
                except:
                        pass
        

f.close() 
