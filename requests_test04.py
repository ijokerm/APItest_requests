"""
【带 json数据 的post请求】使用Requests库，完成 iHRM系统 成功登录。返回 ”令牌数据“。
"""
import requests

resp = requests.post(url="http://ihrm2-test.itheima.net/api/sys/login",
                     # headers={"Content-Type":"application/json"},
                     json={"mobile":"13800000002","password":"123456"})
# 返回结果为网页结果 使用text
# 返回结果为json格式的数据 使用json
print(resp.json())