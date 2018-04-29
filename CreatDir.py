import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
def Creat(url):
    html=urlopen(url)
    bsO=BeautifulSoup(html,'lxml')
    Title=bsO.select('h1')[0].text
    # print(Title)
    return Title
# Creat('http://www.biquge.com.tw/4_4029/')
