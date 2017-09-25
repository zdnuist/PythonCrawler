import requests
from pyquery import PyQuery as pq 
from httpcache import CachingHTTPAdapter
import sys

# sys.path.append("c:\\users\\zd\\appdata\\local\\programs\\python\\python36\\lib")

def getPage():
    s = requests.Session()
    cacheAdapter = CachingHTTPAdapter()
    s.mount("https://", cacheAdapter)
    content = s.get('https://developer.android.google.cn/topic/libraries/architecture/adding-components.html')
    # print(cacheAdapter.cache._cache.items())
    # print(content.headers)
    b = pq(content.text)
    items = b("code")
    # print(items)
    for item in items:
        print(item.text)

print(getPage())