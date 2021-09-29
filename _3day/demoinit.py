# DemoInit.py 

class Demo:
    #메서드 오버로드를 지원 안함 
    #파이썬은 메서드 오버로드 지원(X)
    def __init__(self, id=0, name=""):
        self.id = id 
        self.name = name 

    def print(self):
        print("{0} : {1}".format(self.id, self.name) )

#인스턴스
d1 = Demo()
d2 = Demo(id=100)
d3 = Demo(id=200, name="전우치")

d1.print()
d2.print()
d3.print()
