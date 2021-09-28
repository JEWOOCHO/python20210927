# 파이썬 실습 2일차


d = {1:"apple", 2:"banana", 3:"orange"}
e = [v.upper() for v in d.values()]

print(e)

print(list(range(10)))

_1st = list(range(1,11))
_2st = [i**2 for i in _1st if i > 5 ]

print(_2st)


