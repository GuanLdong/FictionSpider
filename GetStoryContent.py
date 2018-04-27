from urllib.request import urlopen
from bs4 import BeautifulSoup
def GetContent(url):
    html=urlopen(url)
    bsObj=BeautifulSoup(html,'lxml')
    cont=bsObj.select('div["id=content"]')[0]
    Title=bsObj.select('h1')[0]
    list=[]
    list.append(Title.text)
    list.append(cont.text)
    # print(list[0])
    return list
# GetContent('http://www.biquge.com.tw/4_4029/2349288.html')