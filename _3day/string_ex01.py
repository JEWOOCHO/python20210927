# DemoStr.py 

#print( dir(str) )

# strA = "python is powerful"
# print( len(strA) )
# print( strA.capitalize() )
# print( strA.count("p") )
# print( "MBC2580".isalnum() )
# print( "MBC2580".isdecimal() )
# print( "2580".isdecimal() )

#앞뒤에 공백문자 제거(크롤링을 할 경우) 
strB = "<<<  spam,and ham  >>>"
print(strB)
#문자열을 전처리(손이 많이 간다)
result = strB.strip("<>")
result = result.replace("spam", "spam egg")
result = result.replace(",", " ")
print(result)
print("---리스트---")
lst = result.split()
print( lst )
# print("---하나의 문자열----")
# print( " ".join(lst) )


