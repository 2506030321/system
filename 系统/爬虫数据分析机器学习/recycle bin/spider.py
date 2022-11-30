from distutils.filelist import findall
from wsgiref import headers
import requests
from alive_progress import alive_bar
import re


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
headers1={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
List=[]
with alive_bar(len(List)) as bar:
    for i in range(10):
        i+=1
        url=("https://you.ctrip.com/sight/xian7/s0-p%d.html#sightname") %i
        html=requests.get(url,headers=headers)
        html.encoding='utf-8'
        html=html.text
        reg =r'<a target="_blank" href="(.*?)" title=".*?">.*?</a>'
        # reg=re.compile('<a target="_blank" href=".*?" title=".*?">(.*?)</a>',re.S)
        # pattern2=re.compile('<a target="_blank" href="(.*?)" title=".*?">.*?</a>',re.S)
        travel_area=re.findall(reg,html)
        # travel_url=re.findall(pattern2,html)
        List=List+travel_area
        file=open('spyder.txt',mode='w')
        for url in List:
            file.write(url+'\n')  
        bar()      
        file.close()
        
        