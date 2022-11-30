from lib2to3.pgen2 import driver
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'}
regScenic=r'<a target="_blank" href="(.*?)" title=".*?">(.*?)</a>'
cityDataCode='xian7'
for page in range(1,5):
    url=('https://you.ctrip.com/sight/%s/s0-p%d.html#sightname') %(cityDataCode,page)
    htmlCity=requests.get(url,headers=headers)
    htmlCity.encoding='utf-8'
    htmlCity=htmlCity.text
    scenicData=re.findall(regScenic,htmlCity)
    for urlInfo,nameInfo in scenicData:
        driver=webdriver.Chrome()
        driver.get(urlInfo)
        regCommentNumber='<div class="baseInfoMain">.*?<span class="hover-underline">(.*?)<!-- -->条点评</span>.*?</div>'
        commentNumber=re.findall(regCommentNumber,driver.page_source)
        commentPage=int(commentNumber[0])
        if commentPage>=3000:
            for i in range(1,301):
                reg=r'<div class="commentDetail">(.*?)</div>'
                comment=re.findall(reg,driver.page_source)
                f=open(nameInfo+'.txt',mode='a',encoding="utf-8")
                f.write(str(comment)+'\n')    
                s=driver.find_element(By.XPATH,'//*[text()="下一页"]')
                driver.execute_script("arguments[0].click();",s)
        elif 0<commentPage<3000:
            page=int(commentPage/10) 
            for i in range(1,page):
                reg=r'<div class="commentDetail">(.*?)</div>'
                comment=re.findall(reg,driver.page_source)
                f=open(nameInfo+'.txt',mode='a',encoding="utf-8")
                f.write(str(comment)+'\n')    
                s=driver.find_element(By.XPATH,'//*[text()="下一页"]')
                driver.execute_script("arguments[0].click();",s)
        else:
            break

            
