from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re
list=[]
driver = webdriver.Chrome()
driver.get('https://you.ctrip.com/sight/xian7/1444.html')
for i in range(1,301):
    reg=r'<div class="commentDetail">(.*?)</div>'
    comment=re.findall(reg,driver.page_source)
    f=open('comment.txt',mode='a',encoding="utf-8")
    f.write(str(comment)+'\n')    
    s=driver.find_element(By.XPATH,'//*[text()="下一页"]')
    driver.execute_script("arguments[0].click();",s)

   
# print(driver.page_source)
# driver.implicitly_wait(3)
# input=driver.find_element(By.ID,"search_sight_name")
# input.send_keys("华山")
# input.send_keys(Keys.ENTER)
# spot=driver.find_element(By.XPATH,"//a[@title='华山']")
# driver=spot.click()
# for i in range(10):
#     ActionChains(driver).key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
#     time.sleep(0.2)







