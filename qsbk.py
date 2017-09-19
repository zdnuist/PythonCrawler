import requests
import sys
import re
import time

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.stories = []
        self.enable = True
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        self.headers = { 'User-Agent' : self.user_agent }
    

    def getPageContent(self,pageIndex):
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        r = requests.get(url , headers = self.headers)
        return r.text

    def getPageItems(self,pageIndex):
        pageContent = self.getPageContent(pageIndex)
        # print(pageContent)
        items = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',pageContent,re.M | re.S)
        _prefix = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        filePath = 'qsbk_'+_prefix
        f = open(filePath,'w+',encoding = 'utf-8')
        print(sys.getdefaultencoding())
        index = 0
        for item in items:
            # print('***********************************************')
            # print(str(item.strip()))
            # self.stories.append(item.strip())
            strItem = item.strip()
            f.write(str(index))
            f.write("\n")
            f.write(strItem)
            f.write("\n")
            index = index + 1

        f.flush()
        f.close()


        


qsbk = QSBK()
qsbk.getPageItems(2)
