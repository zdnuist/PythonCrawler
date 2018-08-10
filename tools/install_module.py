import os

os.chdir("G:/git_src/18_03/gitS/jade-press")
fileExist = os.path.exists("log1.txt")
if fileExist :
    os.remove("log1.txt")

os.system("node app 2> log1.txt")

fo = open("log1.txt", "r+", encoding="utf-8")
str = fo.read(100)
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

first = str.find("'")
print(first)
second = str.find("'" , first+1)
print(second)
moulename = str[first+1:second]
print(moulename)

os.system("cnpm install " + moulename)

