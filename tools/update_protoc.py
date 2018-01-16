import os

os.chdir( "C:/zdnuist/loocha_git/proto/") 
os.system("git pull ")

os.chdir( "G:\\zdnuist\\github\\ProtocGen\\") 
os.system("gradlew copyProtocFromSVN")
os.system("gradlew build")
os.system("gradlew copyProtoc")