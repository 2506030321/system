# 爬取评论数据为post请求，需要提交表单数据
import requests
import json


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
url=('https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList')
# 提交申请的表单
for Id in range(70000,75682):
  form= {
    "arg": {
      "channelType": 2,
      "collapseType": 0,
      "commentTagId": 0,
      "pageIndex": 3,
      "pageSize": 10,
      "poiId": Id,
      "sourceType": 1,
      "sortType": 3,
      "starType": 0
    },
    "head": {
      "cid": "09031028412671326042",
      "ctok": "",
      "cver": "1.0",
      "lang": "01",
      "sid": "8888",
      "syscode": "09",
      "auth": "",
      "xsid": "",
      "extension": []
    }
  }
  ex=Exception('d对zhe')
  html=requests.post(url,data=json.dumps(form),headers=headers)
  json_data=html.json()
  json_comment=json_data['result']
  json=json_comment['items']
  for comment in json:
    j=comment['content']
    print(j)
  raise 

