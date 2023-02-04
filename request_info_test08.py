"""
获取url：resp.url
获取 响应 状态码 ：resp.status_code
获取Cookie：resp.cookies
获取 响应头：resp.headers
获取 响应体：
    # 文本格式：resp.text
    # json格式：resp.json()  注意：不是所有响应结果都可以转json格式 会报JSONDecodeError
"""
import requests

resp = requests.get("https://www.baidu.com")
print("获取URL：",resp.url)
print("获取响应状态码：",resp.status_code)
print("获取Cookie：",resp.cookies)
print("获取响应头：",resp.headers)
print("获取响应体--文本：",resp.text)
print("获取响应体--json：",resp.json())