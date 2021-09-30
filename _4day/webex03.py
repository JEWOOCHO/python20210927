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
f = open("D:\WORK\python\_4day\webtoon.txt", "wt", encoding="utf-8")          
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

