#encoding=utf8
import urllib.request
import bs4
import time

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

for n in range(1,3):
    url = 'http://www.xicidaili.com/nn/'+str(n)
    req = urllib.request.Request(url,headers=header)
    res = urllib.request.urlopen(req).read()

    print(n)
    soup = bs4.BeautifulSoup(res,'lxml')
    ips = soup.findAll('tr')
    f = open("D:\Fiction\IPGet.txt", "w")
    time.sleep(3)

    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\t"+tds[5].contents[0]+"\n"
        # print (tds[1].contents[0]+"\n"+tds[5].contents[0])
        f.write(ip_temp)
    f.close()
