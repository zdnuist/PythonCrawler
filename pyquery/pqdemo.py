#https://pythonhosted.org/pyquery/
#pip3 install pyquery
from pyquery import PyQuery as pq 
import sys
sys.path.append("..")
from qsbk import QSBK

pageContent = QSBK().getPageContent(3)
# print(pageContent)
b = pq(pageContent)
print(b("title").text().strip())
print(b("img").attr("src"))

lis = b("img")
print(lis)

for li in lis.items():
    print(li.html())