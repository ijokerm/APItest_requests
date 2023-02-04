"""
发送 获取验证码请求
从验证码的结果 提取cookie
发送登陆请求：URL、请求头、请求体。携带cookie，得到响应结果
打印响应结果
"""
import requests

resp_c = requests.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")
my_cookie = resp_c.cookies
resp = requests.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                    # headers={"Content-Type": "application/x-www-form-urlencoded"},
                    data={"username": "13012345678", "password": "12345678", "verify_code":"8888"},
                    cookies=my_cookie)
print(resp.json())

