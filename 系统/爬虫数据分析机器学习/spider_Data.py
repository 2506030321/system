from contextlib import nullcontext
from operator import mod
import requests
import re
import os
def transList(list):
    if len(list)!=0:
        for i in list:
            return i
    else:
        return 'none'
cityDataCode=['yulin485','yanan423','tongchuan907','weinan908','xianyang632','xian7','baoji422','shangluo906','hanzhong486','ankang545']
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'}
for city in cityDataCode:
    for page in range(1,300):
        url_scenicSpot=('https://you.ctrip.com/sight/%s/s0-p%d.html#sightname')  %(city,page)
        html=requests.get(url_scenicSpot,headers=headers) 
        html=html.text
        reg =r'<a target="_blank" href="(.*?)" title=".*?">(.*?)</a>'
        list=re.findall(reg,html) 
        for url2,addresss in list:
            html2=requests.get(url2,headers=headers)
            html2.encoding='utf-8'
            html2=html2.text
            reg_scenicSpot='<div class="baseInfoMain">.*?<div class="title"><h1>(.*?)</h1>.*?</div>'
            reg_score='<div class="baseInfoMain">.*?<div class="heatScoreText">(.*?)</div>.*?</div>'
            reg_comment='<div class="baseInfoMain">.*?<span class="hover-underline">(.*?)<!-- -->条点评</span>.*?</div>'
            reg_heat='<div class="baseInfoMain">.*?<p class="commentScoreNum">(.*?)</p>.*?</div>'
            reg_address='<div class="baseInfoMain">.*?<p class="baseInfoText">(.*?)</p>.*?</div>'
            scenicsSpot=re.findall(reg_scenicSpot,html2)
            score=re.findall(reg_score,html2)
            comment=re.findall(reg_comment,html2)
            heat=re.findall(reg_heat,html2)
            address=re.findall(reg_address,html2)
            with open('das.txt',mode='a',encoding='utf-8') as f:
                 f.write(addresss+' '+url2+' '+transList(score)+' '+transList(comment)+' '+transList(heat)+' '+transList(address)+'\n')
                
        





