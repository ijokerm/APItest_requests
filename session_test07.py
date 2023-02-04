"""
借助session重新实现 上述 TPshop商城登录，并获取 “我的订单” 页面数据。
实现步骤：
1.创建一个session实例
2.使用session实例调用 get方法，调用 发送验证码请求 --不需要获取cookie
3.使用session实例调用 post方法，调用 登录 请求 --无需携带cookie
4.使用session实例调用 get方法，调用 查看订单请求 --无需携带cookie
"""
import requests
session = requests.Session()

resp_v = session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")
resp = session.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                    data={"username": "13012345678", "password": "12345678", "verify_code": "8888"})
print(resp.json())

resp_o = session.get(url="http://tpshop-test.itheima.net/Home/Order/order_list.html")
print(resp_o.text)






