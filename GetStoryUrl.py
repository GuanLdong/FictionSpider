from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
def UrlGet(url):
    UrlCon=[]
    html=urlopen(url)
    bsObj=BeautifulSoup(html,'lxml')
    list=bsObj.select('div[id="list"]')[0].findAll('a')
    for i in list:
        UrlCon.append("http://www.biquge.com.tw"+str(i.get('href')))
    # for n in UrlCon:
    #     print(n)
    print(UrlCon[4])
    return UrlCon
# UrlGet('http://www.biquge.com.tw/4_4029/')
