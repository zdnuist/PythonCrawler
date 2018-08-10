import os
import shutil



os.chdir( "C:/zdnuist/loocha_git/proto/") 
os.system("git pull ")

os.chdir( "G:\\zdnuist\\github\\ProtocGen\\") 

path = "G:\\zdnuist\\github\\ProtocGen\\app\\src\\main\\proto\\"

try:
    shutil.rmtree(path)
    print('clean success')
except:
    print("done")

folder = os.path.exists(path)  
if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹  
    os.makedirs(path) 

os.system("gradlew copyProtocFromSVN")
os.system("gradlew clean build")
os.system("gradlew copyProtoc")