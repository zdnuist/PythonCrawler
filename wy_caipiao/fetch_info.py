import requests
from pyquery import PyQuery as pq
import time


class FetchInfo:

    def __init__(self):
        print('init')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        self.headers = { 'User-Agent' : self.user_agent }
        self.ignoreList = ['我的','个人','如何','帮助','意见','网站','支付','地图','购买','消息','政策','信息','网易','定制','红包','这里','<']

    def getPageInfo(self,url):
        r = requests.get(url , headers = self.headers)
        return r.text

    def getAllLinkInfo(self,content):
        b = pq(content)
        linkList = b("a")


        _prefix = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        filePath = 'zcw_'+_prefix
        f = open(filePath,'w+',encoding = 'utf-8')

        for li in linkList.items():
            _href = li.attr('href')
            _html = li.html()
<<<<<<< HEAD
            isIngore = False

            for item in self.ignoreList:
                if not _html or _html.find(item) != -1:
                    isIngore = True
            
            if isIngore == False:
                if _href and _html:
                    print(_href +"|" +_html)
                    f.write(_href +"|" +_html)
                    f.write("\n")
=======
            if _href and _html:
               print(_href +"|" +_html)
               f.write(_href )
               f.write("\n")
>>>>>>> fix url

        f.flush()
        f.close()

if __name__=='__main__':
    fetchInfo = FetchInfo()
    url = 'http://www.zhcw.com/xinwen/'
    # url = 'http://cai.163.com/'
    content = fetchInfo.getPageInfo(url)
    fetchInfo.getAllLinkInfo(content)
