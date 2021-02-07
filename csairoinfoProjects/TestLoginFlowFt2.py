import requests
import json

host = "https://logincenter-ft2.amwaynet.com.cn/auth/Token"
appId = "/amwaynews"
appSecret = "/3f952615-2ce3-4a5a-b756-e9a87feb152df4ba4367-90eb-4554-863f-111111111111"
url=host+appId+appSecret
res = requests.get(url)
print(res.text)
print(res.elapsed.total_seconds())
jsonDic = json.loads(res.text)
accessToken = jsonDic['accessToken']
Authorization = "Bearer "+accessToken
print("*" * 50)



url = "https://logincenter-ft2.amwaynet.com.cn/sso/api/v6/userticket"
headers = {
'Authorization':Authorization,
}
postData={
  "ada": "363333"
}
res = requests.post(url=url,json=postData,headers=headers)
print(res.text)
print(res.elapsed.total_seconds())
jsonDic = json.loads(res.text)
data = jsonDic['data']
jws = data['jws']
print("*" * 50)



url = "http://apift2-newcommerce.amwaynet.com.cn/member-center/v1/userinfo/query/ada"
headers = {
'jws':jws,
}
postData={
  "ada": "363333"
}
res = requests.post(url=url,json=postData,headers=headers)
print(res.text)
print(res.elapsed.total_seconds())
print("*" * 50)