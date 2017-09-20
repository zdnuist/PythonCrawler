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
        print(soup.title.string)

qsbk_bs = QSBK_BS()
qsbk_bs.start()