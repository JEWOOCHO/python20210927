#try error 처리
# Try1.py 
def divide(a,b):
    return a/b 

#에러 처리(예외적인 상황)
try:
    #함수 호출
    result = divide(5,2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
else:
    print("결과:{0}".format(result))
finally:
    print("한번 더 체크")


print("전체 코드 실행 종료")