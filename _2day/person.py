#파이썬 클래스 연습


class persion:
    num = 0
    def __init__(self, _name='노 네임'):
        self.name = _name
        persion.num += 1
    def print(self):
        print("My name is {0}".format(self.name))


persion.newtitle = "new title"
p1 = persion()
p2 = persion("전우치")
p1.newtitle = "xx"
p1.print()
p2.print()

print(p1.newtitle)
print(p2.newtitle)
print(p1.num)



