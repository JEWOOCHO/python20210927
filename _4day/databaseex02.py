# db2.py 
#커밋을 한 경우 
import sqlite3
#먼저 메모리에만 저장(임시)
#con = sqlite3.connect(":memory:")
#데이터베이스 파일에 저장
con = sqlite3.connect("D:\WORK\python\_4day\sample.db")

#커서 객체를 생성
cur = con.cursor()
#테이블 구조를 만들기(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 데이터 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 데이터를 파라메터 처리
name = "gildong"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
#한번에 여러개의 레코드(행)을 입력
datalist = (("tom","010-333"),("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색을 해서 결과 보기 
cur.execute("select * from PhoneBook;")
#다중 라인 주석처리: ctrl + / 
# for row in cur:
#     print(row)
print("---1건---")
print( cur.fetchone() )
print("---2건---")
print( cur.fetchmany(2) )
print("---전체---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )
#정상적으로 종료하기
con.commit() 
#연결을 끊고 나가기 
con.close() 
