# DemoFilter.py 

#함수를 정의
def getBiggerThan20(i):
    return True if i > 20 else False

#필터링하는 조건으로 함수를 넘기기 
lst = [10, 25, 30]
item = filter(getBiggerThan20, lst)
for i in item:
    print(i)