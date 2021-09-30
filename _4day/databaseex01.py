#sql lite3 데이터베이스 연습

# db1.py 
import sqlite3
#먼저 메모리에만 저장(임시)
con = sqlite3.connect(":memory:")
#커서 객체를 생성
cur = con.cursor()
#테이블 구조를 만들기(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 데이터 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 데이터를 파라메터 처리
name = "gildong"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNum))

#검색을 해서 결과 보기 
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
