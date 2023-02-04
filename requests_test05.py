"""
【发送 put、delete请求】使用Requests库发送 ihrm系统 修改员工信息、删除员工信息 请求。
"""
import requests

reqs = requests.put(url="http://ihrm2-test.itheima.net/api/sys/user/1467780995754229760",
                    headers={"Authorization":"Bearer 4c51c601-c3f7-4d1a-a738-7848f2439f45"},
                    json={"username":"齐天大圣"}
                    )

print(reqs.json())