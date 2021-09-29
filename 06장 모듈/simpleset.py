from functools import *

def intersect(*ar):
    return reduce(__intersectSC,ar)

def __intersectSC(listX, listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList = []
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList


a = [1,2,3]
b = [2,3,8]
c = [2,4,6]
d = [2,8,9]
print(a+b, c+d)
e= intersect(a+b,c+d)
f= union(a,b,c,d)
print(e)

