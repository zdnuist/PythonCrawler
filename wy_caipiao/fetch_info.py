import requests
from pyquery import PyQuery as pq
import time


class FetchInfo:

    def __init__(self):
        print('init')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        self.headers = { 'User-Agent' : self.user_agent }

    def getPageInfo(self,url):
        r = requests.get(url , headers = self.headers)
        return r.text

    def getAllLinkInfo(self,content):
        b = pq(content)
        linkList = b("a")


        _prefix = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        filePath = 'caipiao_'+_prefix
        f = open(filePath,'w+',encoding = 'utf-8')

        for li in linkList.items():
            _href = li.attr('href')
            _html = li.html()
            if _href and _html:
               print(_href +"|" +_html)
               f.write(_href +"|" +_html)
               f.write("\n")

        f.flush()
        f.close()

if __name__=='__main__':
    fetchInfo = FetchInfo()
    content = fetchInfo.getPageInfo('http://cai.163.com/')
    fetchInfo.getAllLinkInfo(content)
