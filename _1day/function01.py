# function 연습
#function01.py

def times(a,b):
    return a*b


result = times(5,6)
print("계산된 값은 %d"%(result))


def swap(x, y):
    return y, x

result = swap(swap(3,4), swap(5,6))

print(result)
