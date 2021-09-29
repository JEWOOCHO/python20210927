

f = open("Kalimba.mp3",'rb')

data = f.read()    # bytes
f.close()

f = open('Kalimba-copy.mp3','wb')
f.write(data)
f.close()

#파일 곡명 확인하기 
f = open("Kalimba.mp3",'rb')
f.seek(-128,2)    # 끝에서 128 바이트로 위치 이동
tagdata = f.read(128)
title = tagdata[3:33].decode()
print( title )
f.close() 

# writing str to binary file
mytext = '이 일은 쉬운 일이 아닙니다.'
f = open('mydata.bin','wb')
f.write(mytext.encode())
f.close()

# reading str from binary file
f = open('mydata.bin','rb')
bdata = f.read()
mytext = bdata.decode()
print( mytext )
f.close()

#숫자 데이터를 읽고 쓰기 
import struct

# packing numerical data into bytes
data = struct.pack("idd",1,10.3,-11.3)   # int, float, float

# unpacking bytes to numerical data
(i,x,y) = struct.unpack("idd",data)   # i=1, x = 10.3, y=-11.3
print( i, x, y )

#숫자 데이터를 파일에 읽고 쓰기
# writing data
age = 27              # int
height = 175.2      # float
weight = 71.3       # float

data = struct.pack('idd',age,height,weight)

f = open('mydata.bin','wb')
f.write(data)
f.close()

# reading data
f = open('mydata.bin','rb')
data = f.read()
(age,height,weight) = struct.unpack('idd',data)
print( age, height, weight)

