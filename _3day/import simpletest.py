from simpleset import *


a = [1,2,3]
b = [2,3,8]
c = [2,4,6]
d = [2,8,9]

print(a+b, c+d)
e= intersect(a+b,c+d)
f= union(a,b,c,d)
print(e)
