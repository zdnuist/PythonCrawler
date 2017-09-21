#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
import qsbk
from bs4 import BeautifulSoup

class QSBK_BS:

    def __init__(self):
        self.qsbk = qsbk.QSBK()

    def start(self):
        pageContent = self.qsbk.getPageContent(2)
        soup = BeautifulSoup(pageContent,"html.parser")
        # print(soup.prettify())
        # print(soup.title.string)
        # print(soup.img["src"])
        # print(soup.find_all('img'))
        # print(soup.get_text())
        # print(soup.find_all("div",class_ = 'content'))
        items = soup.find_all("div" , class_ = 'content')
        for item in items:
            try:
                print(item.span.string.strip())
            except:
                print("none")


qsbk_bs = QSBK_BS()
qsbk_bs.start()