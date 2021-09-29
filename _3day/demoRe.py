#demo py
#정규패턴 표현식 연습

# DemoRE.py
#정규표현식(re)
import re 
#내부에 함수 search(), match() 
result = re.match("[0-9]*th", "35th")
#찾은 결과를 매칭 오브젝트
print( result )
result2 = result.group()
print( result2 )
#search()함수와 match()함수 차이점
#match()함수는 정확하게 일치
print( bool(re.match("[0-9]*th", "  35th")) )
#search()함수는 시작, 중간, 종료... 
print( bool(re.search("[0-9]*th", "  35th")) )
#우편번호를 포함
print( bool(re.search("\d{5}", "우리 동네는 52000")) )

result = re.search("\d{4}", "올해는 2021년")
print( result.group() )

#apple이란 단어 완전히 일치와 포함하고 있는냐 
print( bool( re.match("apple", "this is apple")) )
print( bool( re.search("apple", "this is apple")) )


