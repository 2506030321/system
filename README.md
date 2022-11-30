# system
大数据分析系统
# <center>[第一章：项目总体设计](http://www.baidu.com)
# <center>第二章：数据获取
## 2.1：爬取各景点的关系型数据
## 2.2：爬取评论数据（非关系型）
## 2.3：个人基本情况数据
## 2.4: 项目实战（项目数据获取）
### 2.4.1 数据准备
数据一（各市景点详细信息）
|景点|景点Url|评分|评论数|评论url|热度|地址|开放时间|电话|
|-|-|-|-|-|-|-|-|-|-|
根据以上表头爬取各市数据，每个市景点为一张表（10张表）
市区列表=【榆林市，延安市、铜川市、渭南市、咸阳市、西安市、宝鸡市、商洛市、汉中市、安康市】
市区数字代码=[yulin485,yanan423,tongchuan907,weinan908,xianyang632,xian7,baoji422,shangluo906,hanzhong486,ankang545]
以下为python具体代码：
```python
from contextlib import nullcontext
import requests
import re
import os
import io
# 创建一个用于保存数据的文件夹
if os.path.exists('./Data/'):
    os.rmdir('./Data/')
else:
    os.makedirs('./Data/')
# 定义一个将列表转换成'str'的函数
def trans_list(list):
    for i in list:
        if list==[]:
            return
        else:
            return i

cityDataCode=['yulin485','yanan423','tongchuan907','weinan908','xianyang632','xian7','baoji422','shangluo906','hanzhong486','ankang545']
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'}
for city in cityDataCode:
    path_data=('./Data/')
    if os.path.exists('./Data/'+city+'.txt'):
            os.rmdir(path_data+city+'.txt')
    else:
        f=open(path_data+city+'.txt','w')

    for page in range(1,300):
        url_scenicSpot=('https://you.ctrip.com/sight/%s/s0-p%d.html#sightname')  %(city,page)
        html=requests.get(url_scenicSpot,headers=headers) 
        html=html.text
        reg =r'<a target="_blank" href="(.*?)" title=".*?">(.*?)</a>'
        list=re.findall(reg,html)
        print('正在抓取'+str(city)+'市---------------第'+str(page)+'页/共300页')
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
            f.write(addresss+' '+url2+' '+str(trans_list(score))+' '+str(trans_list(comment))+' '+str(trans_list(heat))+' '+str(trans_list(address))+' '+'\n')
            print(addresss,url2,trans_list(score),trans_list(comment),trans_list(heat),trans_list(address))
```
最终爬取结果为（部分截图）:
![](./../Image/详细数据.png)
数据二（各景点评论信息）
存取数据为非关系型的评论数据，存储在文件夹中格式为文本文档（共10个文件夹）
```python
#   代码插入
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
```
最终展示结果（部分截图）:
![](../Image/评论数据.png)
### 2.4.2 数据爬取：
# <center>第三章：数据清洗与分析
## 3.1 数据去空值、重复值
经过爬取数据可以看出，在景点详细信息表中，其爬取数据中有大量的空值。
由于技术原因，当爬取数据量较大是，网页端数据往往会出现重复页面，这导致数据爬取结果中会有重复值
## 3.2：数据分析
### 3.2.1 对评论数据用“jieba”对其分词
### 3.2.2 去除景点评论中的 停用词
### 3.3.3 对处理后的数据进行向量化处理
1. 参考 [b站：词向量](https://www.bilibili.com/video/BV15P4y1Z74r?p=50&share_source=copy_web&vd_source=aadee7d48914d5c9e308c8a76615c644)
```python
from pyexpat import model
import jieba
from gensim.models.word2vec import LineSentence
import logging
from gensim.models import Word2Vec
import gensim.models
from gensim.models import KeyedVectors
from sklearn import model_selection

# str2="今天天气很不错"
# str2=str2.replace("不错","糟糕")
# print(str2)
f=open('秦始皇帝陵博物院(兵马俑).txt',mode="r",encoding='utf-8')
strh=f.read()
strh.strip(',')
list=jieba.lcut(strh,cut_all=False)
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# def tarin_function():
#      new_data = open('fenxi.txt', "r",encoding='UTF-8') #r 只读
#      model = Word2Vec(LineSentence(new_data),vector_size=100,window=5,workers=1000)
#      model.save('new_data.word2vec')
# # tarin_function()
# model = gensim.models.Word2Vec.load("new_data.word2vec")
# print(model.wv.similarity("历史",""))

file=r"Data\wordVector_trainSet\tencent-ailab-embedding-zh-d200-v0.2.0-s.txt"
model = KeyedVectors.load_word2vec_format(file, binary=False)
# print(model.word_vec("华山"))
# print(model.most_similar('历史',topn=30))
# print(model.most_similar('美食',topn=30))
# print(model.most_similar('动物',topn=30))
# print(model.most_similar('娱乐',topn=30))
# print(model.most_similar('运动',topn=30))
# print(model.most_similar('景色',topn=30))
listHistory=['历史']
listFood=['美食']
listAnimal=['动物']
listEntertainment=['娱乐']
listSport=['运动']
listScenic=['景色']
similarHistory=model.n_similarity(list,listHistory)
similarFood=model.n_similarity(list,listFood)
similarAnimal=model.n_similarity(list,listAnimal)
similarEntertainment=model.n_similarity(list,listEntertainment)
similarSport=model.n_similarity(list,listSport)
similarScenic=model.n_similarity(list,listScenic)
print("与文化相关度为"+str(similarHistory))
print("与美食相关度为"+str(similarFood))
print("与动物相关度为"+str(similarAnimal))
print("与娱乐相关度为"+str(similarEntertainment))
print("与运动相关度为"+str(similarSport))
print("与景色相关度为"+str(similarScenic))

```
### 3.3.4 运用K-means算法对其进行聚类
## 3.3：项目实战（项目数据分析）
# <center>第四章: 基于Eharts前后端搭建
前后端代码为此项目上传代码
# <center>第五章：机器学习及KNN算法
## 5.1 KNN算法
机器学习的过程
1. 爬取后端数据，将数据的80%用作训练模型，部分数据如下：

|ID|性别|年龄|爱好|住址（陕西省）|景点|景点类型|Ehart数据
|-|-|-|-|-|-|-|-|-|
|00001|男|34||||
|00002|男|22||
|00003|女|17|
|00004|男|24|
|00005|女|35|
|00006|男|26|
2. 假设k值，并用剩下20%的后端数据对训练模型进行交叉验证
3. 不断改变k值，直至验证数据集准确率达到90%以上
4. 确定k值，确定训练模型
5. 给出一条个人数据，用训练模型对其进行预测，得到其可能会去的景点

|ID|性别|年龄|爱好|住址（陕西省）|
|-|-|-|-|-|-|-|-|-|
|00452|男|27|美食|渭南|
##  5.2 对预测景点进行Ehart图性分析
如图找出预测景点最突出的三个标签
![](../Image/华山Eharts.png)
对其进行三角分析最终得出与预测景点标签类型相似其它所有景点
## 5.3 协同过滤
最后再将个人数据抽取来，对所得到的所有景点进行协同过滤
找出最符合个人的景点top（n）

## 5.4总结
# <center>第六章：总结
