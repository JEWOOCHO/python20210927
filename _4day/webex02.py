# web 예제

# <td>
# 	<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.img','20853','50')">
# 		<img src="https://shared-comic.pstatic.net/thumb/webtoon/20853/50/inst_thumbnail_20853_50.jpg" title="마음의 소리 50화 &lt;격렬한 나의 하루&gt;" alt="마음의 소리 50화 &lt;격렬한 나의 하루&gt;" width="71" height="41" onERROR="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/non71_41.gif'">
# 		<span class="mask"></span>
# 	</a>
# </td>
# <td class="title">
# <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# 		</td>
# <td>


# web2.py
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup


# 주석: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail?titleId=2">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
          
for i in variable(0,5)         
data = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=1")
soup = BeautifulSoup(data, "html.parser")

              
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)


#파일에 저장
f = open("D:\WORK\python\_4day\webtoon.txt", "a+", encoding="utf-8")
for item in cartoons:
    title = item.find("a").text
    print(title.strip() )
    f.write(title.strip() + "\n")

f.write("\n")
f.close()
