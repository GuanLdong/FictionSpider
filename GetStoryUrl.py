from urllib import request
from bs4 import BeautifulSoup
def UrlGet():
    UrlCon=[]
    html=request.urlopen("http://www.biquke.com/bq/20/20672/")

    bsObj=BeautifulSoup(html,'lxml')
    list=bsObj.findAll('a')
    for i in list:
        UrlCon.append("http://www.biquke.com/bq/20/20672/"+str(i.get('href')))
    # for io in range(len(UrlCon)):
    #     print(UrlCon[io])
    return UrlCon
