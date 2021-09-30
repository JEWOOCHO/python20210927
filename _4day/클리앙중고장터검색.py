
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#우리 사이트는 웹봇을 금지 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("D:\WORK\python\_4day\\클리앙.txt", "wt", encoding="utf-8")
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우에는 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        #검색할 태그는 <span data-role='list...'>: class_="title"
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        # <span class="subject_fixed" data-role="list-title-text">
        # 	아이폰 11프로 256 배터리 88% 리퍼만료
	# </span>

        for item in list:
                try:
                        title = item.text.strip() 
                        title = title.replace("\t", "")
                        #정규표현식을 사용해서 검색
                        if (re.search("아이패드", title)):
                                print( title )
                                f.write( title + "\n")
                except:
                        pass
        

f.close() 

