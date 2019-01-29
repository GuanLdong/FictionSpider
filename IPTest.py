from urllib.request import urlopen
from urllib.request import Request
from test.test_urllib import urlopen
import requests
import socket
import redis
def IPTest():
    socket.setdefaulttimeout(3)
    f=open('D:\Fiction\IPGet.txt')
    lines=f.readlines()
    IPList=[]
    url = "http://ip.chinaz.com/getip.aspx"
    for i in range(len(lines)):
        ip=lines[i].strip("\n").split("\t")
        pro={}
        value="http://"+ip[0]+":"+ip[1]
        pro[ip[2]]=value
        IPList.append(pro)
    print(IPList)
    ReList=[]
    for li in IPList:
        try:
            res=requests.get(url,proxies=li)
            print(res)
            ReList.append(li)
        except Exception as a:
            print('\033[1;31;40m')
            print(a)
    return Relist
