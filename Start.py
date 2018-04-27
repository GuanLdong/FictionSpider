import GetStoryUrl
import GetStoryContent
import time
i=GetStoryUrl.UrlGet()
try:
    for num in range(1015,1800):
        String=GetStoryContent.GetContent(i[num])
        Contnum=str(num-37)
        file = open('D:\\Working\\Python\\Practice\\'+Contnum+String[0]+'.txt','a', encoding='utf-8')
        file.write(String[1])
        print(String[0])
        time.sleep(6)
        print("\n")
        file.close()
except Exception as e:
    print(e)
    pass
print("Over")