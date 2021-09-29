

url ="https://github.com/JEWOOCHO/python20210927/tree/main/_3day" + "+ {0:,}".format(3000)

print(url)
filename = "D:\WORK\python\_3day\demo.txt"
f = open(filename , "wt")
f.write(url)
f.close()

f = open(filename, "rt")
read_text = f.read()
f.close()

print(read_text)

