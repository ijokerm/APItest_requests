""" 演示requests请求方法
resp = requests.请求方法(url='URL地址', params={k:v}, headers={k:v},data={k:v}, json={k:v}, cookies='cookie数据'(如：令牌))
请求方法：
get请求 - get()
post请求 - post()
put请求 - put()
delete请求 - delete()
url: 待请求的url - string类型
params：查询参数 - 字典
headers：请求头 - 字典
data：表单格式的 请求体 - 字典
json：json格式的 请求体 - 字典
cookies：cookie数据 - string类型
resp：响应结果
"""
import requests

resp = requests.get(url="http://www.baidu.com")

print(resp.text)