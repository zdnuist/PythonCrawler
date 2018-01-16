import os
import shutil

os.chdir( "C:/zdnuist/loocha_git_ws/Campus") 

path = "log1.txt"
# if os.path.exists(path) == True:
#     print("file deleted")

# os.system("gradlew aTD >> log1.txt")

ignoreList = ['CampusAppUtil.java','Pay','provider','ProcessorPay','ActSlidingFrame.java','ActSliding','ServerResponse.java','NewBaseProcessor','Emoji','SettingHelp','AppUtil.java','AdView','\\util\\','Cookie','\\video\\','\\LoochaTelecom\\', 'DatabaseManager','CampusActivityManager.java','com\\realcloud\\u'  ,'service' , 'UserAvatarView', '\\receiver\\','RedPackage','CampusApplicationLike.java','JScriptObjectInterface.java','AppConfig.java','weex','WebView','Factory','Cookie','http\\down','ActLoochaCampusNav.java','Runnable']

logFile = open('log1.txt' , 'r')
allLines = logFile.readlines()
prefix = '\\src\\'
for line in allLines:
    if line.find(prefix) !=-1 :
        isIngore = False
        # print(line)
        for item in ignoreList:
            if line.find(item) != -1:
                isIngore = True
                # print(item)

        if isIngore == False :
            noPosition = line.index('.java')
            if os.path.exists(line[0:noPosition] + ".java") == True:
                print(line[0:noPosition] + ".java")
                os.remove(line[0:noPosition] + ".java")
                print("delete success")



