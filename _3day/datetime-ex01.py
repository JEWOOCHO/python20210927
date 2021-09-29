
#날짜 시간 연습

# DemoOS.py
#시간을 다루는 모듈
import time 

#print( dir(time) )

print( int(time.time()) )
#10초를 대기해~~ 
#time.sleep(10)

print( time.gmtime() )
print( time.localtime() )

#날짜와 시간을 다루는 경우
from datetime import *

d1 = date(2021, 10, 5)
print( d1 )
d2 = date.today() 
print( d2 )
d3 = timedelta(days=100)
print( d2 + d3 )

import random 

print( random.random() )
print( random.random() )
#수열을 생성하는 함수
lst = list(range(1,46))
print( lst )
random.shuffle(lst)
print( lst )



#파일이름을 다루는 경우
from os.path import * 

print( abspath("python.exe") )
print( basename("c:\\work\\python.exe") )
print( exists("c:\\python38\\python.exe") )

#운영체제에 있는 정보를 출력
import os 

print("운영체제이름:", os.name)
os.system("notepad")

