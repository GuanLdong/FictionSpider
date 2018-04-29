import GetStoryUrl
import GetStoryContent
import CreatDir
import time
import os
url="http://www.biquge.com.tw/0_32/"
i=GetStoryUrl.UrlGet(url)
path = 'D:\\Fiction\\'+str(CreatDir.Creat(url))+'\\'
print(path)
count=0
if os.path.exists(path):
    ls=os.listdir(path)
    for lsiN in ls:
        if os.path.isfile(os.path.join(path,lsiN)):
            count+=1
    print("目前dir中有 "+str(count)+" 章节")
    pass
else:
    os.makedirs(path)
for num in range(count,len(i)):
    try:
        String=GetStoryContent.GetContent(i[num])
        Contnum=str(num)+"_"
        file = open(path+Contnum+String[0]+'.html','w+', encoding='utf-8')
        file.write(String[1])
        print(String[0])
        time.sleep(5)
        file.close()
    except Exception:
        print(Exception)
        pass
print("Over")