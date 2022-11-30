from dataclasses import dataclass
from html.entities import html5
import requests
from wsgiref import headers
import re
from alive_progress import alive_bar
list=[]
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
with alive_bar(len(list)) as bar:
    for i in range(1,3):
        url=("https://you.ctrip.com/sight/xian7/s0-p%d.html#sightname") %i
        html=requests.get(url,headers=headers)
        html.encoding='utf-8'
        html=html.text
        reg=r'<a target="_blank" href="(.*?)" title=".*?">(.*?)</a>'
        travel_adress=re.findall(reg,html)
        list=list+travel_adress
        # print(list)
    for url2,address in list:
        html2=requests.get(url2,headers=headers)
        # print(url2,address)
        html2.encoding='utf-8'
        html2=html2.text
        reg2='<div class="baseInfoMain"><div class="titleView"><div class="title"><h1>(.*?)</h1><div class="titleTips">'
        info=re.findall(reg2,html2)
        print(address,info)
        bar()

        
            
            

    
    

